from flask import Flask, render_template, request
from admin import simple_page
from flaskext.mysql import MySQL
from flask import jsonify
import  json

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'clic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()



cursor.execute("SELECT username FROM adminTable WHERE adminID=1")

username = cursor.fetchall()

userpasswords = []

@app.route("/")
def hello():
    users = json.dumps(username)
    print(users)
    for user in users[0]:
        userpasswords.append(user)

    return str(userpasswords)


@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/home")
def login():
    age = int(request.args.get('age'))
    if age is None:
        return "general"
    elif age <11:
        return "Under 11"
    elif age >= 11 and age <= 14:
        return "11 to 14"
    elif age >= 15 and age <= 17:
        return "15 to 17"
    elif age >= 18 and age <= 25:
        return "18 to 25"
    else:
        return "general"

if __name__ == "__main__":
    app.run(host="0.0.0.0")



