from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine



Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	username = Column(String(20), nullable=False)
	email = Column(String(30), nullable=False)
	password = Column(String(8), nullable=False)

	def to_dict(self):
		return {'id': self.id,
                'username': self.username,
                'email': self.email }




class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(40))
    checked = Column(Boolean(), default=False)
    due_date = Column(String())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='user', cascade='delete-orphan, delete', single_parent=True)

    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'content': self.content,
                'due_date': self.due_date,
                'checked': self.checked,
                'user_id': self.user_id 
                }

engine = create_engine('sqlite:///' + 'todo.db')
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)


