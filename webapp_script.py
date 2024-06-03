from bottle import request, route, run, static_file, template, error
from mysql.connector import connect

# Funktion zur Erstellung von der DatenBank
def connectDB():
    mydb = connect(
      host="web3.kinet.ch",    
      user="omdb_user",
      database="omdb",
      password="QhPSNctsBRgsYOKEbASI"
    )
    return mydb

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root="static")

# Wenn man den Link eingibt, kommt diese Seite
@route('/')
def index():
    return template("../views/index.html", title="Startseite")

# Routing der about page
@route("/about")
def about():
    return template("../views/about.html", title="About")

# Ergebnis nach einer Suche
@route("/search")
def search():
    query = request.query.decode()
    mydb = connectDB()
    mycursor = mydb.cursor(named_tuple=True)
    # print(f"SELECT * FROM movies WHERE name LIKE '%{query.q}%'")
    mycursor.execute(f"SELECT * FROM movies WHERE name LIKE '%{query.q}%' LIMIT 2")
    
    myresult = mycursor.fetchall()
    
    for movie in myresult:
        print("---------")
        for result in movie:
            print(str(result))
    
    mydb.close()
    
    try:
        return template("search.html", movie=myresult)
    except:
        return template("error.html", movie=None)

@route("/serie/<id>")
def film(id):
    return "Du hast Details zur Serie mit der id " + id + " verlangt"

# Sucht man eine Subpage, die es nicht gibt, gibt das einen Fehler.
@error(404)
def error404(error):
    return "Ups, diese Seite gibt es nicht."

run(reloader=True, host='localhost', port=8000)
