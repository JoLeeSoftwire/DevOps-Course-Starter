# DevOps Apprenticeship: Project Exercise

## Getting started

You will need to set up an OAuth App in GitHub to support the app's authentication, see documentation [here](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)
* The homapage URL will be `http://localhost:5000`
* The Authorization callback URL will be `http://localhost:5000/login/callback`
* Make a note of the `client id` and `client secret` for the .env file

You can see the site running (the version on the `master` branch) [here](http://jol-todo-webapp.azurewebsites.net/)

Copy the `.env.template` file to a new file `.env`, and populate it with your mongo database connection string, client id, and client secret.

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
These can be run in a docker container or locally. You will need to run `poetry install` in order to run the tests locally, or build the docker container once with `docker build --target test --tag todoapp-test .` to run tests in docker. 
To run all tests in docker: `docker run --env-file ./.env todoapp-test`. 
To run all the tests locally: `poetry run pytest`

### Unit tests
To run them (and the integration tests) in the docker container: `docker run todoapp-test src/tests`

To run them locally: 
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
