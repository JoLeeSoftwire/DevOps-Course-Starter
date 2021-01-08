#!/bin/bash

poetry run gunicorn --bind=0.0.0.0:$PORT 'src.todolist.app:create_app()'