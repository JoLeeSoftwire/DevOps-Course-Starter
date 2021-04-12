import requests, os
# from random import randint
from flask import Flask, render_template, request, redirect, url_for
from .DbCommunicator import DbCommunicator
from .ViewModel import ViewModel
from .User import User
from flask_login import LoginManager, login_required, login_user
from oauthlib.oauth2 import WebApplicationClient

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
client = WebApplicationClient(CLIENT_ID)

def create_app():
    app = Flask(__name__)
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        endpoint = "https://github.com/login/oauth/authorize"
        # state = randomString(12)
        github_url = client.prepare_request_uri(endpoint)

        return redirect(github_url)

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        return user

    login_manager.init_app(app)

    @app.route('/login/callback')
    def login():
        code = request.args.get('code')
        endpoint = "https://github.com/login/oauth/access_token"
        params = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.post(endpoint, params=params, headers=headers)
        token_json = response.json()
        token = token_json['access_token']
        
        user_endpoint = "https://api.github.com/user"
        auth_header = {
            "Authorization": "Bearer "+token
        }
        user_details = requests.get(user_endpoint, headers=auth_header)
        user = User(user_details['user_id'])
        
        success = login_user(user)
        
        return redirect(url_for('index'))


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

    # def randomString(len):
    #     random_string = ''
    #     for _ in range(len):
    #         random_integer = randint(97, 97+26-1)
    #         random_string += (chr(random_integer))
    #     return random_string

    if __name__ == '__main__':
        app.run(host='0.0.0.0')

    return app
