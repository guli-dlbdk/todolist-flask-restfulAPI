from flask import Flask, render_template, request
from app.models import DBSession

from app.api.todo import api_bp as todo_api_bp
from app.api.user import api_bp as user_api_bp
from app.api.auth import api_bp as auth_api_bp



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xab\x7fe\xb2\xb9\xf5K:\xf8\xe4\x91\xdf\xf0)lk\xc0\xdeg\x8eQp\x17D'




app.register_blueprint(todo_api_bp)
app.register_blueprint(user_api_bp)
app.register_blueprint(auth_api_bp)



@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html')


