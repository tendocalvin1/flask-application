from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.permanent_session_lifetime = timedelta(hours=3)

@app.route('/')
def home():
    return render_template("index.html", content=["Allan","David","Beckham"])


@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session ['user'] = user
        return redirect(url_for("user", usr=user))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template("login.html")

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"

    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash("You have been logged out successfully, {user}!", 'info')
    session.pop('user', None) # This removes the user data from the sessions
    
    return redirect(url_for('login'))
    


# @app.route('/<name>')
# def user(name):
#     return f"Hello, {name}! Welcome to my Embedded Systems project"

# @app.route('/admin')
# def admin():
#     return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(debug=True)
    
    