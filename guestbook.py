from bottle import run, route, template, static_file

@route('/')
def index():
	return template('static/index.html')

@route('/static/<filename:path>')
def static(filename):
	return static_file(filename, root='static')

run()