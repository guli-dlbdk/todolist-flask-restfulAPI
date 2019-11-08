from flask import Flask, abort
from app.models import DBSession,Todo, User





def get_todos():
	db_session = DBSession()
	todos = db_session.query(Todo).all()
	if not todos:
		result = {'message': 'todolist boş'}
	result = [d.to_dict() for d in todos]
	db_session.close()
	return result




def get_todo(todo_id):
	if not todo_id:
		result = {'status': 'error'}
	else:
		db_session = DBSession()
		todo = db_session.query(Todo).filter(Todo.id == todo_id).first()
		if not todo:
			result = {'message': 'todo listede yok'}
		else:
			result = [todo.to_dict()]
		db_session.close()
	return result




def user_todos(user_id):
	if not user_id:
		result = {'status': 'Error'}
	else:
		db_session = DBSession()
		user_todos = db_session.query(Todo).filter(Todo.user_id == user_id).all()
		if not user_todos:
			result = {'message': 'User a ait bir todo yok'}
		result = [d.to_dict() for d in user_todos]
		db_session.close()
	return result



def create_todo(data):
	
	db_session = DBSession()
	new_todo = Todo(title=data['title'], content=data['content'], due_date=data['due_date'],
					checked=data['checked'], user_id=data['user_id'])

	db_session.add(new_todo)
	db_session.commit()

	new_todo = new_todo.to_dict()

	db_session.close()
	print('todo oluşturuldu.', new_todo['id'])
	return new_todo




def update_todo(data):
	db_session = DBSession()
	todo = db_session.query(Todo).filter(Todo.id == data['id']).first()
	if not todo:
		result = {'messages': 'Todo not found'}
	else:
		todo.title = data['title']
		todo.content = data['content']
		todo.due_date = data['due_date']
		todo.checked = data['checked']
		db_session.commit()
		db_session.close()
		result = {'message': 'todo güncellendi.'}

	return result




def delete_todo(todo_id):
	if not todo_id:
		return {'status': 'Error'}
	else:	
		db_session = DBSession()
		todo = db_session.query(Todo).filter(Todo.id == todo_id).first()
		if not todo:
			abort(404,'bu id ye sahip bir todo yok.')
		else:
			db_session.delete(todo)
			db_session.commit()
			db_session.close()
			return {'status': 'OK'}