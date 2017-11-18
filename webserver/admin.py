from flask import Blueprint,render_template,Flask,request
app = Flask(__name__)
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'clic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

cursor.execute("SELECT * FROM adminTable WHERE adminID=1")

username = cursor.fetchall()

userpasswords = []


simple_page = Blueprint('simple_page', __name__, template_folder='./templates/templates')
@simple_page.route('/admin')
def admin():
    return render_template("admin.html")
@simple_page.route('/login')
def login():
        users = username
        print(users)
        for i in range(0, len(users)):
            userpasswords.append([users[i][0], users[i][1].encode('utf-8'), users[i][2].encode('utf-8')])
        return str(userpasswords)
@simple_page.route('/send')
def userLogin():
    user = request.form["user"]
    age = request.form["age"]
    exp = request.form["experience"]
  
    cursor.execute("INSERT INTO pastExperiences (nickname,age,experience) VALUES ('"+user+"','"+age+"','"+exp+"')")
    conn.commit()
    return redirect("/community", code=302)

@simple_page.route('/getexp', methods=['GET'])
def userLogin():
   cursor.execute("select * from pastExperiences")
   experience = []
   username = cursor.fetchall()
   for i in range(0, len(users)):
        userpasswords.append([users[i][0], users[i][1], users[i][2])
        

 
   return jsonify(data=userpasswords)