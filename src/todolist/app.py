import requests, os
from flask import Flask, render_template, request, redirect, url_for, abort
from .DbCommunicator import DbCommunicator
from .ViewModel import ViewModel
from .User import User, Role
from flask_login import LoginManager, login_required, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
client = WebApplicationClient(CLIENT_ID)

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        endpoint = "https://github.com/login/oauth/authorize"
        github_url = client.prepare_request_uri(endpoint)

        return redirect(github_url)

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        return user

    login_manager.init_app(app)

    def requireWriteAccess():
        if current_user.role() == Role.Reader:
            abort(403)
        return

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
        user_details = requests.get(user_endpoint, headers=auth_header).json()
        user = User(user_details['id'])
        
        success = login_user(user)
        
        return redirect(url_for('index'))


    @app.route('/')
    @login_required
    def index():
        tasks = DbCommunicator.get_items()
        has_write_access = current_user.role() == Role.Writer
        item_view_model = ViewModel(tasks, has_write_access)
        return render_template('index.html', data=item_view_model)

    @app.route('/task', methods=['POST'])
    @login_required
    def addTask():
        requireWriteAccess()
        title = request.form.get('title')
        description = request.form.get('description')
        DbCommunicator.add_item(title, description)
        return redirect('/')

    @app.route('/task/<id>', methods=['PUT', 'POST'])
    @login_required
    def completeItem(id):
        requireWriteAccess()
        DbCommunicator.mark_done(id)
        return redirect('/')

    if __name__ == '__main__':
        app.run(host='0.0.0.0')

    return app
