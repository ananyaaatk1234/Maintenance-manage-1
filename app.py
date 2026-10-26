from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/machines")
def machines():
    return "This is the Machines Page"

@app.route("/maintenance")
def maintenance():
    return "This is the Maintenance Page"



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
    