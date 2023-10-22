from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private/")
def private():
    #test user logged in failed
    #so redirects to login
    return redirect(url_for('login'))

@app.route('/login/')
def login():
    return "Now we get username and password"

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)