from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(20), nullable=False)
	email = Column(String(30), nullable=False)
	password = Column(String(8), nullable=False)

	def to_dict(self):
		return {
        		'id': self.id,
                'name': self.name,
                'email': self.email
                }


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    content = Column(String(40), nullable=False)
    checked = Column(Boolean, nullable=True, default=False)
    due_date = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(User)

    def to_dict(self):

        return {
        		'id': self.id,
                'description': self.description,
                'detail': self.detail,
                'due_date': self.due_date,
                'checked': self.checked,
                'user_id': self.user_id
 
                }

engine = create_engine('sqlite:///' + 'todo.db')
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)



