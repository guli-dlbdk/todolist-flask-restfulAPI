from schema import Schema, Use

TODO_SCHEMA = Schema({
    'title': Use(str),
    'content': Use(str),
    'due_date': Use(str),
    'checked': Use(str),
	})


DELETE_TODO_SCHEMA = Schema({
	'id': Use(int),
	})