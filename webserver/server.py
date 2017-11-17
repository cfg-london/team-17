from flask import Flask
from admin import simple_page
app = Flask(__name__)

app.register_blueprint(simple_page)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
