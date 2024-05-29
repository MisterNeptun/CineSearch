from bottle import request, route, run, static_file, template, error
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

@route('/static/<filename>')
def static(filename):
    static_file(filename, root="../static")

# ERKLÄRUNG?
@route('/')
def index():
    return template("../views/index.html", title="Startseite")

# Routing der about page
@route("/about")
def about():
   
    return return template("about.html", title="About")

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

@error(404)
def error404(error):
    return 'DU HSOHN HAST NACH FALSCHEN SACHEN GESUCHT'

run(reloader=True, host='localhost', port=8080)
