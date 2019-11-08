from flask import Flask, Blueprint, request
from flask_restful import Api, Resource
from app.data_schemas import (AUTH_SCHEMA)
from app.modules.users import DBSession, User
from hashlib import sha512


api_bp = Blueprint ('auth_record_api', __name__)
api = Api(api_bp)


class AuthResource(Resource):

	def post(self):
		request_data = request.get_json()
		if (not AUTH_SCHEMA.validate(request_data)):
			return {'status': 'error'}
		db_session = DBSession()
		password = sha512(request_data['password'].encode('utf-8')).hexdigest()
		user = db_session.query(User).filter(User.email == request_data['email'], User.password == password).first()
		if not user:
			return {'message':'user bulunamadı'}

		return user.username





api.add_resource(AuthResource, '/api/auth')