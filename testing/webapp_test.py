from bottle import request, route, run

@route('/')
def index():
    return 'Hello World!!!!!!'

@route("/about")
def about():
    page = "Wir haben diese App im EF-Informatik erstellt!"
    return page

@route("/serie/<id>")
def film(id):
    return "Du hast Details zur Serie mit der id " + id + " verlangt"

@route("/search")
def search():
    query = request.query.decode()
    return "Du willst nach " + query.q + " suchen?"

run(reloader=True, host='localhost', port=8080)
