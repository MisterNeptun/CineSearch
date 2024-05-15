from bottle import request, route, run, static_file, template
import mysql.connector

def connect():
    mydb = mysql.connector.connect(
      host="web3.kinet.ch",    
      user="omdb_user",
      database="omdb",
      password="QhPSNctsBRgsYOKEbASI"
    )
    return mydb

@route('/')
def index():
    return template("startseite.html", title="Startseite")

@route("/about")
def about():
    page = "Wir haben diese App im EF-Informatik erstellt!"
    return page

@route("/serie/<id>")
def film(id):
    return "Du hast Details zur Serie mit der id " + id + " verlangt"
@route('/movie')
def movie():

    mydb = connect()
    mycursor = mydb.cursor(named_tuple=True)    
    mycursor.execute("SELECT * FROM movies WHERE name LIKE '%Titanic%'")

    myresult = mycursor.fetchone()
    
    mydb.close()
    print(myresult)
    return template("movie.html", movie=myresult)
    


@route("/search")
def search():
    query = request.query.decode()
    return "Du willst nach " + query.q + " suchen?"

run(reloader=True, host='localhost', port=8080)
