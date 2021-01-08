#!/bin/bash

# PORT=${PORT:1}

poetry run gunicorn --bind=0.0.0.0:$PORT 'src.todolist.app:create_app()'