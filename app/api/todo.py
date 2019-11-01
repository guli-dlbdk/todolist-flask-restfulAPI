from flask import Flask, jsonify, request, Response
from datetime import datetime
import json



app = Flask(__name__)

todos = [
		
   {
    'id': 1,
    'name': 'Alısveris',
    'content': 'Yapılması gereken alısverisler',
    'due_date': datetime(2019,5,1)

    },

  {
	'id': 2,
    'name': 'Toplantı',
    'content': '12 de toplantı yapılacak.',
    'due_date': datetime(2019,4,10)

    },

  {
    'id': 3,
    'name': 'Sinema',
    'content': 'Salı sinemaya gidilecek',
    'due_date': datetime(2019,8,11)
         
    }
]

DEFAULT_PAGE_LIMIT = 5

class Todo(Resource):

	#GET /todos
	@app.route('/todos')
	def get_todos():
		return jsonify({'todos': todos})


	#POST /todos
	#{
	#  'id': 4,
	#  'name': 'Ajanda',
	#  'content': 'Ajanda alınacak',
	#  'due_date': datetime(2020,8,20)            
	#}


	def validTodoObject(todoObject):
		if ("id" in todoObject and "name" in todoObject and "content" in todoObject and "due_date" in todoObject):
			return True
		else:
			return False


	#/todos/id

	@app.route('/todos', methods=['POST'])
	def add_todo():
		request_data = request.get_json()
		if(validTodoObject(request_data)):
			new_todo = {
				"id": request_data['id'],
				"name": request_data['name'],
				"content": request_data['content'],
				"due_date": request_data['due_date']
			}
			todos.insert(0, new_todo)
			response = Response("",201, mimetype='application/json')
			response.headers['Location'] = "/todos/" + str(new_todo['id'])
			return response
		else:
			invalidTodoObjectErrorMsg = {
				"error": "Invalid todo object passed in request",
				"helpString": "Data passed in similar to this { 'id': 5, 'name':'Toplantı', 'content': 'Salı toplantı yapılacak', 'due_date':'2020,3,18' }"
			}

			response = Response(json.dumps(invalidTodoObjectErrorMsg), status=400, mimetype='application/json');
			return response



	#GET /todos/id
	@app.route('/todos/<int:id>')
	def get_todo_by_id(id):
		return_value = {}
		for todo in todos:
			if todo["id"] == id:
				return_value = {
					'name':todo["name"],
					'content':todo["content"]
				}
		response = Response(status=404)
		return response



	#PUT /todos/id
	#{
	# 'name': 'Toplantı',
	# 'content': 'Bilet alınacak',
	# 'due_date': '2030,3,5'
	#}

	def valid_put_request_data(request_data):
		if("id" in request_data and "name" in request_data 
			and "content" in request_data and "due_date" in request_data):
			return True
		else:
			return False


	@app.route('/todos/<int:id>', methods=['PUT'])
	def replace_todo(id):
		request_data = request.get_json()
		if(not valid_put_request_data(request_data)):
			invalidTodoObjectErrorMsg = {
				"error": "Invalid todo object passed in request",
				"helpString": "Data passed in similar to this { 'id': 5, 'name':'Toplantı', 'content': 'Salı toplantı yapılacak', 'due_date':'2020,3,18' }"
			}

		response = Response(json.dumps(invalidTodoObjectErrorMsg), status=400, mimetype='application/json');
		return response

		new_todo = {
			'id':id,
			'name': request_data['name'],
			'content': request_data['content'],
			'due_date': request_data['due_date']
		}

		i = 0
		for todo in todos:
			currentId =todo["id"]
			if currentId == id:
				todos[i] = new_todo
			i += 1
		response = Response("", status=204)
		return response



	#PATCH /todos/id
	#{
	# 'name': 'Toplantı'
	#}

	#PATCH /todos/id
	#{
	# 'due_date': '2020,4,8'
	#}


	@app.route('/todos/<int:id>', methods=['PATCH'])
	def update_todo(id):
		request_data = request.get_json()
		updated_todo = {}
		if("name" in request_data):
			updated_todo["name"] = request_data["name"]
		if("due_date" in request_data):
			updated_todo["due_date"] = request_data["due_date"]
		for todo in todos:
			if todo["id"] == id:
				todo.update(updated_todo)
		response = Response("", status=204)
		response.headers['Location'] = "/todos/" + str(id)
		return response





	#DELETE /todos/id
	#Body :{'name':'test'}

	@app.route('/todos/<int:id>', methods=['DELETE'])
	def delete_todo(id):
		i = 0
		for todo in todos:
			if todo["id"] == id:
				todos.pop(i)
			i += 1
		return "";





api.add_resource(Todo, '/api/todo')