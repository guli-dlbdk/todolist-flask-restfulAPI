from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import Date
from sqlalchemy import DateTime


Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)
	email = Column(String(30), nullable=False)
	password = Column(String(8), nullable=False)

	def to_dict(self):
		return {'id': self.id,
                'name': self.name,
                'email': self.email }


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(40))
    checked = Column(Boolean, default=False)
    due_date = Column(DateTime())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'content': self.content,
                'due_date': self.due_date,
                'checked': self.checked,
                'user_id': self.user_id }

engine = create_engine('sqlite:///' + 'todo.db')
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)



