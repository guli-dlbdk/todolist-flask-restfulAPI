from app.models import DBSession, Users
from hashlib import sha512
from sqlalchemy import desc


def create_user(data):
    db_session = DBSession()
    print(data)
    user = db_session.query(Users).filter(
        Users.email == data['email']).first()

    if user:
        return {'status': 'user error',
                'message': 'message'}
    password = sha512(data['password'].encode('utf-8')).hexdigest()
    new_user = Users(name=data['name'],
                     password=password,
                     email=data['email'])

    try:
        db_session.add(new_user)
        db_session.commit()
        result = {'status': 'OK',
                  'user': data['name']}
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def get_users():
    try:
        db_session = DBSession()

        users = db_session.query(Users).all()
        result = [d.to_dict() for d in users]

    except Exception:
        result = []

    db_session.close()
    return result


def get_user(id):
    try:
        db_session = DBSession()
        user = db_session.query(Users).get(id)
        if not user:
            result = None
        else:
            result = [user.to_dict()]
    except Exception:
        result = []

    db_session.close()
    return result


def update_user(user_id, data):
    data = {k: data[k] for k in data if k in ['name', 'email',
                                              'password', 'new_password']}
    db_session = DBSession()

    user = db_session.query(Users).get(user_id)
    password = sha512(data['password'].encode('utf-8')).hexdigest()

    if (not user or user.password != password):
        return {'hata': '1'}

    if (user.password == password and data['new_password'] != ''):
        new_password = sha512(
            data['new_password'].encode('utf-8')).hexdigest()
        user.name = data['name']
        user.email = data['email']
        user.password = new_password

    elif (user.password == data['password'] and data['new_password'] == ''):
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
    else:
        return {'hata': '2'}

    db_session.commit()
    db_session.close()

    return {'status': 'OK',
            'user': user_id}


def delete_user(user_id, data):
    if not user_id:
        return{'status': 'error'}

    db_session = DBSession()
    user = db_session.query(Users).get(user_id)
    password = sha512(data['password'].encode('utf-8')).hexdigest()
    if (not user or data['email'] != user.email or
            password != user.password):
        return{'status': 'error'}
    db_session.query(Users).filter(Users.id == user_id).delete()
    db_session.commit()
    db_session.close()

    return {'status': 'OK'}
