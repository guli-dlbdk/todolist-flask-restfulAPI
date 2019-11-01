
'''from flask import Flask,render_template
from flask_session import Session

app = Flask(__name__, instance_relative_config=False)

Session(app)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')



'''

from flask import Flask, render_template, request
from flask_session import Session


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'reds209ndsldssdsljdsldsdsljdsldksdksdsdfsfsfsfis'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdf'

# Flask's default flask_session tool, are more flexible and as long as
# you aren't storing secrets, just fine security-wise.

#Session(app)  #Server-side Session 

#The second possibility is to create the object once and configure the application later:
#sess = Session()
#sess.init_app(app)


'''app.register_blueprint(user_api_bp)
app.register_blueprint(todo_api_bp)
app.register_blueprint(auth_api_bp)'''


@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html',)


