from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import sqlalchemy
app = Flask(__name__)


loggedin = False





@app.route('/')
def index():
    if not loggedin:
        return redirect(url_for('LoginOrSignup'))
    return render_template('welcome.html')

@app.route('/LoginOrSignup',methods=['GET','POST'])
def LoginOrSignup():
    return render_template('loginSignup.html')



@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        for user in users:
            if request.form['username'] == user[0] or request.form['username'] == user[1] or request.form['password'] == user[1] == True:
                return redirect(url_for('home'))
            else:
                error = 'Invalid cedentials. Please try again'
    return render_template('login.html', error=error)

@app.route('/signup')
def signup():

    return render_template('signup.html')
@app.route('/confirmation', methods=['GET','POST'])
def confirmation():
    return 'Please confirm email'


@app.route('/home')
def home():
    return 'hello world'



if __name__ == '__main__':
    app.run(debug=True)