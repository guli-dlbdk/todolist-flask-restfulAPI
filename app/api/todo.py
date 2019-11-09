from flask import Flask, Blueprint, request, abort
from flask_restful import Api, Resource
import json
from app.modules.todos import (get_todos, get_todo, user_todos, create_todo, update_todo, delete_todo)
from app.data_schemas import (TODO_SCHEMA, TODO_UPDATE_SCHEMA)
from schema import SchemaError




api_bp = Blueprint('todo_record_api', __name__)
api = Api(api_bp)

class TodoResource(Resource):

	def get(self):
		todo_id = request.args.get('id', None)
		user_id = request.args.get('user_id', None)
		print('todo_id:', todo_id)
		print('user_id:', user_id)
		if todo_id:
			todos = get_todos()
			if not todos:
				return {'message': 'TodoList boş'}
			todo = get_todo(todo_id)
			if not todo:
				return {'message': 'Todo listede yok'} 
			return {'todo': todo}
		result = user_todos(user_id)
		if not result:
			return {'message': 'User Todo yok'}
		return {'todos': result}





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



	def put(self):
		request_data = request.get_json()
		if(not TODO_UPDATE_SCHEMA.validate(request_data)):
			return {'status': 'error'}
		todo_id = request.args.get('id', None)

		print('update id:', todo_id)

		if not todo_id:
			return {'message': 'todo id yok'}
		request_data['id'] = todo_id
		updated_todo = update_todo(request_data)
		return {'status': 'OK',
		        'update_todo': updated_todo}
		
		
	


	def delete(self):
		todo_id = request.args.get('id')
		if not todo_id:
			return {'message': 'todo id not found'}
		else:
			todo = delete_todo(todo_id)
			return {'status': 'OK',
					'message': 'Todo was deleted'}





api.add_resource(TodoResource, '/api/todo')
