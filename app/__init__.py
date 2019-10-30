from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/gulistan/Project/todo/todo.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


Session(app)


@app.route('/')
@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html', title='LOG IN', )

