FROM python:3.8.5-buster as base

WORKDIR /todo-app

RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

EXPOSE 5000

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false --local
RUN poetry install

FROM base as development
# Configure for local development
ENTRYPOINT [ "poetry" ]
CMD ["run", "flask", "run", "--host=0.0.0.0"]
# build with command: docker build --target develoment --tag todolist:dev .
# run command: docker run --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/src,target=/todo-app/src todolist:dev

FROM base as production
# Configure for production
COPY . .
RUN poetry install

ENTRYPOINT poetry run gunicorn --bind=0.0.0.0:$PORT src.todolist.app:create_app()
# build with command: docker build --target production --tag todolist:prod .
# run command: docker run --env-file .env -p 5000:8000 todolist:prod

FROM base as test
# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
 apt-get install ./chrome.deb -y &&\
 rm ./chrome.deb
# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
echo "Installing chromium webdriver version ${LATEST}" &&\
curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
apt-get install unzip -y &&\
unzip ./chromedriver_linux64.zip

COPY . .
RUN poetry install
ENTRYPOINT [ "poetry", "run", "pytest" ]
