from flask import Blueprint,render_template, Flask, session,request
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

cursor.execute("SELECT * FROM userTable")

username = cursor.fetchall()
userpasswords = []

user_login_blueprint = Blueprint('user_login_blueprint', __name__, template_folder='./templates/templates')
@user_login_blueprint.route('/user/login', methods=['POST'])
def userLogin():

    users = username
    print(users)
    for i in range(0, len(users)):
        userpasswords.append([users[i][0], users[i][1].encode('utf-8'), users[i][2].encode('utf-8')])


    __inputUsername = request.form['username']
    __inputPassword = request.form['password']

    for users in userpasswords:
        valid = 0
        if (__inputUsername == users[1]) and (__inputPassword == users[2]):
            valid = 1
            break

    if valid == 1:
        session['username'] = __inputUsername
        return 'Logged in as ' + str(__inputUsername) + '<br>'
    else:
        return 'You arent logged in'
@user_login_blueprint.route('/user')
def page():
    return render_template("userLogin.html")



