from flask import Flask, jsonify, request
from datetime import datetime


def validTodoObject(todoObject):
	if ("id" in todoObject 
			and "name" in todoObject 
				and "content" in todoObject):

		return True
	else:
		return False

valid_object = {
	'id': 5,
	'name': 'F',
	'content': 'Hello'
	#'due_date': datetime(2020,10,6)
}

missing_id = {
	'name': 'F',
	'content': 'Hello'
	#'due_date': datetime(2020,10,6)	
}

missing_name = {
	'id': 5,
	'content': 'Hello'
	#'due_date': datetime(2020,10,6)	
}

missing_content = {
	'id': 5,
	'name': 'F'
	#'due_date': datetime(2020,10,6)
}

''' 'missing_due_date = {
  'content': 'Hello'
  'due_date': datetime(2020,10,6)
}'''

empty_dictionary = {}





















