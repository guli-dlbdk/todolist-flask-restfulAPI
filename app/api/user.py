from flask import Flask, Blueprint, request, abort
from flask_restful import Api, Resource
import json
from app.modules.users import (create_user, get_user, get_users, delete_user)
from app.data_schemas import (USER_SCHEMA)
from schema import SchemaError




api_bp = Blueprint('user_record_api', __name__)
api = Api(api_bp)


class UserResource(Resource):

	def post(self):
		request_data = request.get_json()
		if(not USER_SCHEMA.validate(request_data)):
			return {'status': 'error'}
		else:

			new_user = {
				'username': request_data['username'],
				'email': request_data['email'],
				'password': request_data['password']
				}
			user = create_user(new_user)
			return {'user': user}



	def get(self):
		user_id = request.args.get('id')
		print('user_id:', user_id)
		if user_id:
			user = get_user(user_id)
			return {'status': 'OK',
					'user': user}

		users = get_users()
		if not users:
			abort(404, 'user yok')
		else:
			return {'status': 'OK',
					'users': users}
	


	def delete(self):
		user_id = request.args.get('id')
		if not user_id:
			return {'message': 'user id not found'}
		else:
			deleted_user = delete_user(user_id)
			return {'status': 'OK',
					'message': 'User was deleted'}


	


api.add_resource(UserResource, '/api/user')