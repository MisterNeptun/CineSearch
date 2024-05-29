from bottle import request, route, run, static_file, template
from mysql.connector import connect

# Funktion zur Erstellung von der DatenBank
def connectDB():
    mydb = mysql.connector.connect(
      host="web3.kinet.ch",    
      user="omdb_user",
      database="omdb",
      password="QhPSNctsBRgsYOKEbASI"
    )
    return mydb

# ERKLÄRUNG?
@route('/')
def index():
    return template("../views/startseite.html", title="Startseite")

# Routing der about page
@route("/about")
def about():
    page = "Wir haben diese App im EF-Informatik erstellt!"
    return page

# ISt das nötig?
"""
# Rückgabe der Id-Webseite
@route("/serie/<id>")
def film(id):
    return "Du hast Details zur Serie mit der id " + id + " verlangt"
"""


@route('/movie')
def movie():

    mydb = connectDB()
    mycursor = mydb.cursor(named_tuple=True)    
    mycursor.execute("SELECT * FROM movies join trailers on movies.id=trailers.movie_id WHERE name LIKE "%Titanic%" ORDER BY movies.revenue DESC")

    myresult = mycursor.fetchone()
    
    mydb.close()
    
    print(myresult)
    return template("movie.html", movie=myresult)

@route("/search")
def search():
    query = request.query.decode()
    return "Du willst nach " + query.q + " suchen?"

run(reloader=True, host='localhost', port=8080)
