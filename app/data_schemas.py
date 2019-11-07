from schema import Schema, Use


USER_SCHEMA = Schema({
	'username': Use(str),
	'email': Use(str),
	'password': Use(str),
	})


TODO_SCHEMA = Schema({
	'title': Use(str),
	'content': Use(str),
	'due_date': Use(str),
	'checked': bool,
	'user_id': int,

	})

TODO_UPDATE_SCHEMA = Schema({
	'title': Use(str),
	'content': Use(str),
	'due_date': Use(str),
	'checked': bool,
	})


