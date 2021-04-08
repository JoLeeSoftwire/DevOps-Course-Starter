import requests
import os
from random import randint
from flask import Flask, render_template, request, redirect, url_for
from .DbCommunicator import DbCommunicator
from .ViewModel import ViewModel
from flask_login import LoginManager, login_required

def create_app():
    app = Flask(__name__)
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        CLIENT_ID = os.environ.get('CLIENT_ID')
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        endpoint = "https://github.com/login/oauth/authorize"
        state = randomString(12)
        github_url = endpoint+"?client_id="+CLIENT_ID+"&state="+state

        # redirect = requests.get(endpoint, params=params)
        return redirect(github_url)
        # prepare_request_uri()

    @login_manager.user_loader
    def load_user(user_id):
        return None

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        tasks = DbCommunicator.get_items()
        item_view_model = ViewModel(tasks)
        return render_template('index.html', data=item_view_model)

    @app.route('/task', methods=['POST'])
    def addTask():
        title = request.form.get('title')
        description = request.form.get('description')
        DbCommunicator.add_item(title, description)
        return redirect('/')

    @app.route('/task/<id>', methods=['PUT', 'POST'])
    def completeItem(id):
        DbCommunicator.mark_done(id)
        return redirect('/')

    def randomString(len):
        random_string = ''
        for _ in range(len):
            random_integer = randint(97, 97+26-1)
            random_string += (chr(random_integer))
        return random_string

    if __name__ == '__main__':
        app.run(host='0.0.0.0')

    return app
