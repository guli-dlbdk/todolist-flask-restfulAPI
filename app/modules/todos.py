from app.models import DBSession, Todos
from sqlalchemy import desc







def create_todo(data):
    db_session = DBSession()

    new_todo = Todos(description=data['description'], 
                    detail=data['detail'],
                    due_date=data['due_date'],
                    user_id=data['user_id'])

    try:
        db_session.add(new_todo)
        db_session.commit()

        result = {'status': 'OK',
                  'todo': data['detail']}
        print(result)
    except:
        db_session.rollback()
        result = {'status': 'error'}

    db_session.close()
    return result


def get_todos():
    db_session = DBSession()

    todos = db_session.query(Todos).order_by(desc(Todos.id)).all()
    result = [d.to_dict() for d in todos]

    except Exception:
        result = []

    db_session.close()
    return result


def get_todo(todo_id):
    try:
        db_session = DBSession()
        todo = db_session.query(Todos).filter(Todos.id == todo_id).all()

        if not todo:
            result = None
        else:
            result = [todo.to_dict()]

    except Exception:
        result = []
    db_session.close()
    return result


def delete_todo(todo_id):
    if not (todo_id):
        result = {'status': 'error'}
    try:
        db_session = DBSession()
        todo = db_session.query(Todos).get(todo_id)
        db_session.delete(todo)
        db_session.commit()
        db_session.close()

    except Exception:
        result = {'status': 'OK'}
    return result



def update_todo(data):
    try:
        db_session = DBSession()
        todo = db_session.query(Todos).filter(Todos.id == data['id']).first()
        
        if not todo:
            result = {'status': 'error',
                    'message': 'No such todo.'}

        todo.description=data['description']
        todo.detail=data['detail']
        todo.due_date=data['due_date']
        todo.checked=data['checked']
         
        db_session.commit()
        db_session.close()

        result =  [todo.to_dict()]

    except Exception:
        result = []

    return result
