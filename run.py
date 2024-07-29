from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://omar:omar@localhost/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the ToDo model
class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home():
    todos = ToDoItem.query.all()
    return render_template('home.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        new_todo = ToDoItem(task=task)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = ToDoItem.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['POST'])
def update_todo(id):
    todo = ToDoItem.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
