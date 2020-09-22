FROM python:3.8.5-buster

WORKDIR /todo-app

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

EXPOSE 5000

COPY . .
RUN poetry install

ENTRYPOINT [ "poetry" ]
CMD ["run", "gunicorn", "todolist.app:create_app()"]
