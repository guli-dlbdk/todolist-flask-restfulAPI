from flask import Flask, Blueprint, request, abort
from flask_restful import Api, Resource
from datetime import datetime
import json
from app.modules.todos import (get_todo, get_todos, update_todo, delete_todo)
from app.data_schemas import (TODO_SCHEMA, DELETE_TODO_SCHEMA)
from schema import SchemaError




api_bp = Blueprint('todo_record_api', __name__)
api = Api(api_bp)

class TodoResource(Resource):

	#GET /todo-todos
	def get(self):
		todo_id = request.args.get('id')
		if todo_id:
			todo = get_todo(todo_id)
			return {'status': 'OK',
					'todo': todo}

		todos = get_todos()
		if not todos:
			abort(404)
		return {'status': 'OK',
				'todos': list(todos)}



	#POST /todos
	#{
	#  'id': 4,
	#  'name': 'Ajanda',
	#  'content': 'Ajanda alınacak',
	#  'due_date': datetime(2020,8,20)            
	#}

	def post(self):
		request_data = request.get_json()
		print ('request', request_data)
		if(TODO_SCHEMA.validate(request_data)):
			print('schema doğrulandı')
			new_todo = {
				'title': request_data['title'],
				'content': request_data['content'],
				'due_date': request_data['due_date'],
				'checked': request_data['checked']
			}
			
			todo = create_todo(new_todo)
			return {'status': 'OK',
					'todo': todo }
		else:
			return {'status': 'Error',
					'message':'schema error'}



	

	#PUT /todos/id
	#{
	# 'name': 'Toplantı',
	# 'content': 'Bilet alınacak',
	# 'due_date': '2030,3,5'
	#}

	def put(self):
		request_data = request.get_json()
		if(not TODO_SCHEMA(request_data)):
			return {'status': 'error',
					'message': 'Missing or incorrect parameters'}

		update_todo = update_todo(request_data)
		return {'status': 'OK',
				'update_todo': update_todo}





	#PATCH /todos/id
	#{
	# 'name': 'Toplantı'
	#}

	#PATCH /todos/id
	#{
	# 'due_date': '2020,4,8'
	#}

	# def patch(self):
	# 	request_data = request.get_json()
	# 	updated_todo = {}
	# 	if(request_data['title']):
	# 		updated_todo['title'] = request_data['title']
	# 	if(request_data['due_date']):
	# 		updated_todo['due_date'] = request_data['due_date']
	# 	for todo in todos:
	# 		if todo['id'] == request_data['id']
	# 			todo.update(updated_todo)
	# 	return {'status': 'OK',
 #                'update_todo': updated_todo}

		



	#DELETE /todos/id
	#Body :{'name':'test'}
	def delete(id):
		todo_id = request.args.get('id')
		todo = delete_todo(todo_id)
		return {'status': 'OK',
				'message': 'Todo was deleted'}





api.add_resource(TodoResource, '/api/todo')