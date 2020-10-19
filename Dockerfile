FROM python:3.8.5-buster as base

WORKDIR /todo-app

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

ENTRYPOINT [ "poetry" ]
CMD ["run", "gunicorn", "--bind=0.0.0.0", "src.todolist.app:create_app()"]
# build with command: docker build --target production --tag todolist:prod .
# run command: docker run --env-file .env -p 5000:8000 todolist:prod
