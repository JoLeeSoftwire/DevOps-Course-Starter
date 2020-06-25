from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    tasks = session.get_items()
    return render_template('index.html', tasks=tasks)

@app.route('/task', methods=['POST'])
def addTask():
    title = request.form.get('title')
    session.add_item(title)
    return redirect('/')

@app.route('/task/<id>', methods=['PUT', 'POST'])
def completeItem(id):
    session.mark_done(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
