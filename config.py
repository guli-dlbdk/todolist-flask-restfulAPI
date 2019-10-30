"""App configuration."""
from os import environ


class Config:
	SECRET_KEY = b'v$\x0c11\xbcB\x89\\\xc3$%\x8d\x06\xb2\x82\x0b\xaa\xf5#\x179\xe23'
	
app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/gulistan/Project/todo/todo.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
