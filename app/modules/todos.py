from flask import Flask,  jsonify
from app.models import DBSession,Todo
from app.data_schemas import (TODO_SCHEMA)


def get_todos():
	db_session = DBSession()
	todos = db_session.query(Todo).all()
	db_session.close()
	return jsonify({'todos': todos})
	


def get_todo(todo_id):
	if not todo_id:
		return {'status': 'Error'}
	else:
		db_session = DBSession()
		todo = db_session.query(Todo).filter(Todo.id == todo_id).all()
		if not todo:
			return {'messages':'Todo not found.'}
		todo = [d.to_dict() for d in todo]
		db_session.close()



def create_todo(data):
	db_session = DBSession()
	new_todo = Todo(title=data['title'], content=data['content'],
				    checked=data['checked'], due_date=data['due_date'],
				    user_id=data['user_id'])
	try:
		db_session.add(new_todo)
		db_session.commit()
		result = {'status': 'OK',
				  'todo': data }
	except:
		db_session.rollback()
		return {'status': 'Error'}
	db_session.close()
	return result



def update_todo(data):
	db_session = DBSession()
	todo = db_session.query(Todo).filter(Todo.id == data['id']).first()
	if not todo:
		return {'status': 'Error',
				'messages': 'Todo not found'}
	else:
		todo.title = data['title'] 
		todo.content = data['content']
		todo.due_date = data['due_date']
		todo.checked = data['checked']
	
	db_session.commit()
	db_session.close()
	return {'status': 'OK',
			'todo': todo_id}

	result = [todo.to_dict()]






def delete_todo(todo_id):
	if not todo_id:
		return {'status': 'Error'}
	db_session = DBSession()
	todo = db_session.query(Todo).get(todo_id)
	db_session.delete(todo)
	db_session.commit()
	db_session.close()
	return {'status': 'OK'}



