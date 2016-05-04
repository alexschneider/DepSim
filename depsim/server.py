from bottle import route, post, run, template, request

@route('/')
def index():
    return template('index')

@post('/simulate')
def simulate():
    print(request.files.get('model'))
    return '<p>hai</p>'

run(host='localhost', port=8080)
