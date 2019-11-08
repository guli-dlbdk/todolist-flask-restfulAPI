from flask import Flask, abort
from app.models import DBSession, User
from hashlib import sha512



def create_user(data):
	db_session = DBSession()
	user = db_session.query(User).filter(User.email == data['email']).first()
	if user:
		abort(404,'bu email kullanılmış.')
	else:
		password = sha512(data['password'].encode('utf-8')).hexdigest()
		new_user = User(username=data['username'], email=data['email'], password=password)
	try:
		db_session.add(new_user)
		db_session.commit()
		result = [new_user.to_dict()]
	except:
		db_session.rollback()
		result = {'status': 'error'}
	db_session.close()
	print('user oluşturuldu')
	return result




def get_user(user_id):
	db_session = DBSession()
	user = db_session.query(User).filter(User.id == user_id).first()
	if not user:
		result = {'status': 'error'}
	else:
		result = [user.to_dict()]

	db_session.close()
	return result


def get_users():
	try:
		db_session = DBSession()
		users = db_session.query(User).all()
		if not users:
			result = {'message': 'User yok'}
		result =[d.to_dict() for d in users]
	except:
		result = {'status': 'error'}
	db_session.close()
	return result





def delete_user(user_id):
	if not user_id:
		return{'status': 'error'}
	else:
		db_session = DBSession()
		user = db_session.query(User).filter(User.id == user_id).first()
		if not user:
			abort(404,'bu id ye sahip bir user yok.')
		db_session.delete(user)
		db_session.commit()
		db_session.close()
		return {'message': 'user silindi'}
		

