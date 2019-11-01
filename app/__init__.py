from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from flask import Flask,render_template



app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True





'''from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/gulistan/Project/todo/todo.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
'''


@app.route('/index')
def index():
	return render_template('index.html')


