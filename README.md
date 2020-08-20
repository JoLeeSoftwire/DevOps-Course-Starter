# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, populate the `src/.env` file with your trello api credentials and board ID. Then navigate into the `src` folder, and start the Flask app by running:
```bash
$ flask run
```

You should see output similar to the following:
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
### Unit tests
navigate to the the `src/tests` directory
run `pytest` to run all the unit and integration tests
run `pytest <filename>` to run the unit tests in that file

### Integration tests
navigate to the `src/tests` directory
run `pytest integration_test.py`

### End to end tests
you will need to have installed Chrome web browser, and the Selenium [chrome driver](https://chromedriver.chromium.org/downloads)
navigate to the `src/tests_e2e` folder
run `pytest`