from flask import Flask, render_template, request, redirect, url_for
# import trello_api as trello
from TrelloApi import TrelloApi

app = Flask(__name__)

@app.route('/')
def index():
    tasks = TrelloApi.get_items()
    return render_template('index.html', tasks=tasks)

@app.route('/task', methods=['POST'])
def addTask():
    title = request.form.get('title')
    description = request.form.get('description')
    TrelloApi.add_item(title, description)
    return redirect('/')

@app.route('/task/<id>', methods=['PUT', 'POST'])
def completeItem(id):
    TrelloApi.mark_done(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
