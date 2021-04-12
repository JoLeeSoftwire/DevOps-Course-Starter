from flask import Flask, render_template, request, redirect, url_for
from .DbCommunicator import DbCommunicator
from .ViewModel import ViewModel

def create_app():
    app = Flask(__name__)

    @app.route('/')
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

    if __name__ == '__main__':
        app.run(host='0.0.0.0')

    return app
