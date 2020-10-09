# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses docker to run in a suitably configured container. You will need Docker installed.

Copy the `.env.template` file to a new file `.env`, and populate it with your trello api credentials and board ID. 

Then start the Flask app by running:
```bash
$ docker-compose up
```

Alternatively, run `poetry install` then `poetry run flask run` locally

You should (eventually) see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running Tests
Note these do not currently run in the container, you will need to `poetry install` locally to run the tests

### Unit tests
navigate to the the `src/tests` directory
run `poetry run pytest` to run all the unit and integration tests
run `poetry run pytest <filename>` to run the unit tests in that file

### Integration tests
navigate to the `src/tests` directory
run `pytest integration_test.py`

### End to end tests
you will need to have installed Chrome web browser, and the Selenium [chrome driver](https://chromedriver.chromium.org/downloads)
navigate to the `src/tests_e2e` folder
run `poetry run pytest`