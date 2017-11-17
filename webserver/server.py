from flask import Flask,request,render_template
from admin import simple_page

app = Flask(__name__)

app.register_blueprint(simple_page)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/home")
def login():
    try:
        age = int(request.args.get('age'))
    except TypeError as e:
        return "general"
    if age <11:
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
