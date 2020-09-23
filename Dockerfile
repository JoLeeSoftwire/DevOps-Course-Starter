FROM python:3.8.5-buster as base

WORKDIR /todo-app

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

EXPOSE 5000

FROM base as production

# Configure for production
COPY . .
RUN poetry install

ENTRYPOINT [ "poetry" ]
CMD ["run", "gunicorn", "--bind=0.0.0.0", "todolist.app:create_app()"]

FROM base as development

# Configure for local development
# files by bind mount
RUN mkdir /root/.cache
RUN mkdir /root/.cache/pypoetry
RUN mkdir /root/.cache/pypoetry/virtualenvs

ENTRYPOINT [ "poetry" ]
CMD ["run", "flask", "--bind=0.0.0.0", "run"]
