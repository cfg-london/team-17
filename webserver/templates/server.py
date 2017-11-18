from flask import Flask, render_template, request, send_from_directory
from admin import simple_page
from userlogin import user_login_blueprint
from usersignup import user_signup_blueprint
from flaskext.mysql import MySQL
from flask import jsonify
import  json

mysql = MySQL()
app = Flask(__name__,static_url_path='')

app.secret_key = "rnamd"
app.register_blueprint(simple_page)
app.register_blueprint(user_login_blueprint)
app.register_blueprint(user_signup_blueprint)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/community")
def comm():
    return render_template("community.html")




@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/imgs/<path:path>')
def send_img(path):
	return send_from_directory('imgs',path)


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

@app.route("/signup")
def signup():
	return render_template("signup.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0")



