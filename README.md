# DevOps Apprenticeship: Project Exercise

## Getting started

Copy the `.env.template` file to a new file `.env`, and populate it with your trello api credentials and board ID. 

The project can use docker to run in a suitably configured container. For this you will need Docker installed.

Then start the Flask app by running:
```bash
$ docker-compose up --build
```

There is also a vagrantfile, to run the project in vagrant
to use this run `vagrant up` in the project root

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
These can be run in a docker container or locally
you will need to run `poetry install` in order to run the tests locally, or build the docker container once with `docker build --target test --tag todoapp-test .` to run tests in docker
To run all tests in docker: `docker run --env-file ./.env todoapp-tests`
To run all the tests locally: `poetry run pytest`

### Unit tests
to run them (and the integration tests) in the docker container: `docker run todoapp-test src/tests`

to run them locally:
navigate to the the `src/tests` directory
run `poetry run pytest` to run all the unit and integration tests
run `poetry run pytest <filename>` to run the unit tests in that file

### Integration tests
to run them in the docker container, see the instructions for running unit tests in the container

to run them locally:
navigate to the `src/tests` directory
run `pytest integration_test.py`

### End to end tests
to run them in the docker container: `docker run --env-file ./.env todoapp-test src/tests_e2e`

to run them locally:
you will need to have installed Chrome web browser, and the Selenium [chrome driver](https://chromedriver.chromium.org/downloads)
navigate to the `src/tests_e2e` folder
comment out lines 43-47 (line 44 optional) in `e2e_tests.py` and uncomment line 48 (don't forget to reverse this if you switch to running them in a container)
run `poetry run pytest`

## Documentation
see the `docs` folder for 3 of the C4 diagrams
