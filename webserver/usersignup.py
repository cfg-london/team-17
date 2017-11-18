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

userpasswords = []

user_signup_blueprint = Blueprint('user_signup_blueprint', __name__, template_folder='./templates/templates')
@user_signup_blueprint.route('/signup', methods=['POST'])
def userLogin():
    __inputUsername = request.form['username']
    __inputPassword = request.form['password']
    __age = request.form['age']
    __typec = request.form['cancerType']
    __stage = request.form['stage']
    print "INSERT INTO userTable (username,password,age,cancerType,stage) VALUES ('"+__inputUsername+"','"+__inputPassword+"','"+__age+"','"+__typec+"','"+__stage+"')"
    cursor.execute("INSERT INTO userTable (username,password,age,cancerType,stage) VALUES ('"+__inputUsername+"','"+__inputPassword+"','"+__age+"','"+__typec+"','"+__stage+"')")
    conn.commit()
    return redirect("/user", code=302)




