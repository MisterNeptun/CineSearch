
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
 
@route('/')

def index():

    import random

    zahl=random.randint(1,240108)

    mydb = connectDB()

    mycursor = mydb.cursor(named_tuple=True)    

    mycursor.execute(str("SELECT * FROM movies WHERE id LIKE '%")+ str(zahl) + str("%'"))
 
    myresult = mycursor.fetchone()

    mydb.close()

    print(myresult)

    return template("../views/index.html", vorschlag=myresult)

# Routing der about page

@route("/about")

def about():

    return template("../views/about.html", title="About")
 
 
@route("/search")

def search():


    try:

        query = request.query.decode()

        mydb = connectDB()

        mycursor = mydb.cursor(named_tuple=True)

        print(str("SELECT * FROM movies WHERE name LIKE '%")+query.q+str("%'"))

        mycursor.execute(str("SELECT * FROM movies WHERE name LIKE '%")+ query.q + str("%' OR id LIKE '%")+query.q+ str("%' LIMIT 1000"))

        myresult = mycursor.fetchall()


        mydb.close()

        for i in myresult:

            print(i)

        if len(myresult)<1:

            return template("error.html")

        return template("movie.html", movie=myresult)

    except:

        return template("error.html")

@route("/movie")

def movie():


    try:

        query = request.query.decode()

        mydb = connectDB()

        mycursor = mydb.cursor(named_tuple=True)

        mycursor.execute(str("SELECT * FROM movies WHERE id LIKE '%")+query.q+ str("%'"))

        myresult = mycursor.fetchone()


        mydb.close()

        mydb = connectDB()

        mycursor2 = mydb.cursor(named_tuple=True)

        mycursor2.execute(str("SELECT * FROM abstracts WHERE movie_id = '")+query.q+ str("'"))

        myresult2 = mycursor2.fetchone()

        mydb.close()

        if myresult2 is None:

            

            from collections import namedtuple

            Row = namedtuple("Row", "text")

            myresult2 = Row(text="No Description")


            
         
        mydb = connectDB()

        mycursor3 = mydb.cursor(named_tuple=True)

        mycursor3.execute(str("SELECT * FROM trailers WHERE movie_id = '")+query.q+ str("'"))

        myresult3 = mycursor3.fetchone()

        mydb.close()
        if myresult3 is None:
            from collections import namedtuple

            Row = namedtuple("Row", "key")

            myresult3 = Row(key="dQw4w9WgXcQn")
       
       




        return template("result.html", movie=myresult,abstracts=myresult2,key=myresult3)

    except:

        return template("error.html")

@error(404)

def error404(error):

    return template("../views/404.html", title="404 Error")
 
run(reloader=True, host='localhost', port=8000)
 
 
