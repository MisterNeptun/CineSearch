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

# ERKLÄRUNG?
@route('/')
def index():
    return template("../views/index.html", title="Startseite")

# Routing der about page
@route("/about")
def about():
    return template("../views/about.html", title="About")

@route("/search")
def search():
    query = request.query.decode()
    mydb = connectDB()
    mycursor = mydb.cursor(named_tuple=True)
    print(str("SELECT * FROM movies WHERE name LIKE '%")+query.q+str("%'"))
    mycursor.execute(str("SELECT * FROM movies WHERE name LIKE '%")+ query.q + str("%'"))
    
    myresult = mycursor.fetchone()
    
    mydb.close()
    
    try:
        return template("movie.html", movie=myresult)
    except:
        return template("fehler.html")

@error(404)
def error404(error):
    return 'DU HAST NACH FALSCHEN SACHEN GESUCHT'

run(reloader=True, host='localhost', port=8000)
