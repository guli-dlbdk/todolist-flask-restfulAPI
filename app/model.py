
from flask import Flask
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'v$\x0c11\xbcB\x89\\\xc3$%\x8d\x06\xb2\x82\x0b\xaa\xf5#\x179\xe23'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()



class Users(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)
	email = Column(String(30), nullable=False)
	password = Column(String(8), nullable=False)

	def to_dict(self):

		return { 
    			'id': self.id,
                'name': self.name,
                'email': self.email
                }



class Todos(Base):
	__tablename__ = 'todos'

	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)
	content = Column(String(40))
	checked = Column(Boolean, nullable=True, default=0)
	due_date = Column(DateTime(), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

    def to_dict(self):

    	return { 
    			'id': self.id,
                'name': self.name,
                'content': self.content,
                'checked': self.checked,
                'due_date': self.due_date,
                'user_id': self.user_id
                }
	


engine = create_engine(SQLALCHEMY_DATABASE_URI)
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)

