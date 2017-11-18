from flask import Blueprint,render_template, Flask, session,request,redirect,jsonify
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
userpasswords = []


exp = Blueprint('exp', __name__, template_folder='templates')
@exp.route('/send', methods=['POST'])
def userLogin():
    user = request.form["user"]
    age = request.form["age"]
    exp = request.form["experience"]
  
    cursor.execute("INSERT INTO pastExperiences (nickname,age,experience) VALUES ('"+user+"','"+age+"','"+exp+"')")
    conn.commit()
    return redirect("/community", code=302)







