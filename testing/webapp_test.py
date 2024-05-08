from bottle import request, route, run, static_file, template

@route('/')
def index():
    return return template("startseite_html.html", title="Startseite")

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
