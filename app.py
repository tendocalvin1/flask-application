from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content=["Allan","David","Beckham"])


@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
       user = request.form['nm']
       session ['user'] = user
       return redirect(url_for("user", usr=user))
    else: 
        return render_template("login.html")

@app.route('/user')
def user(usr):
    return f"<h1>{usr}</h1>"


# @app.route('/<name>')
# def user(name):
#     return f"Hello, {name}! Welcome to my Embedded Systems project"

# @app.route('/admin')
# def admin():
#     return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(debug=True)
    
    