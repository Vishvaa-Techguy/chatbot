from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

if __name__== "___main___":
    app.run(debug=True)