from flask import Flask, Blueprint, request, abort
from flask_restful import Api, Resource
import json
from app.modules.todos import (get_todo, get_todos, create_todo, update_todo, delete_todo)
from app.data_schemas import (TODO_SCHEMA)
from schema import SchemaError




api_bp = Blueprint('todo_record_api', __name__)
api = Api(api_bp)

class TodoResource(Resource):

	def get(self):
		todo_id = request.args.get('id')
		print('todo_id:', todo_id)
		if not todo_id:
			todos = get_todos()
			if not todos:
				return {'status': 'error',
						'message': 'todo list boş'}	
			else:
				return {'status': 'OK',
						'todos': todos}
		todo = get_todo(todo_id)
		if not todo:
			return {'status': 'error',
					'message': 'todo listede yok'}

		return {'todos': todo}





	def post(self):
		request_data = request.get_json()
		if(not TODO_SCHEMA.validate(request_data)):
			return {'status': 'error'}
		else:
			user_id = request_data['user_id']
			print('user id', user_id)
			todo = create_todo(request_data)
			return {'status': 'OK',
					'todo': todo}


		
#put çalışmıyor  bakılacak
	def put(self):
		request_data = request.get_json()
		if(not TODO_SCHEMA.validate(request_data)):
			return {'status': 'error',
					'message': 'Missing or incorrect parameters'}

		updated_todo = update_todo(request_data)
		return {'status': 'OK',
				'update_todo': update_todo}
		
	


	def delete(self):
		todo_id = request.args.get('id')
		if not todo_id:
			return {'message': 'todo id not found'}
		else:
			todo = delete_todo(todo_id)
			return {'status': 'OK',
					'message': 'Todo was deleted'}





api.add_resource(TodoResource, '/api/todo')