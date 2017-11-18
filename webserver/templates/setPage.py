from flask import Blueprint,render_template, Flask, session,request,redirect
from flask.ext.session import Session
from flaskext.mysql import MySQL

app = Flask(__name__)


mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'clic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

cursor.execute("SELECT * FROM postTable")

username = cursor.fetchall()
userpasswords = []

set_page = Blueprint('set_page', __name__, template_folder='templates')
@set_page.route('/edit', methods=['POST'])
def userLogin():

     users = username
    print(users)
    for i in range(0, len(users)):
        userpasswords.append([users[i][0], users[i][1], users[i][2],users[i][3],users[i][4],users[i][5],users[i][6])
        
   i1= request.form['item1'] or userpasswords[2]
   i2= request.form['item2'] or userpasswords[3]
   i3= request.form['item3'] or userpasswords[4]
   i4= request.form['item4'] or userpasswords[5]
   i5= request.form['item5'] or userpasswords[6]

   query = "UPDATE pageTable SET item1 = '"+i1+"' item2 = '"+i2+"' item3 = '"+i3+"' item4 = '"+i4+"' item5 = '"+i5+"' where age = "+userpasswords[0]+")"

    cursor.execute(query)
    conn.commit()
    return redirect("/home?age="+userpasswords[1], code=302)
@set_page.route("/edit")
def useredit():
    return render_template("admin-edit.html")




