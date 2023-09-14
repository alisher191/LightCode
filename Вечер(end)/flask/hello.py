from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, LoginManager, UserMixin, login_required, logout_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'
app.secret_key = 'secretkey'
login_manager = LoginManager(app)

db = SQLAlchemy(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    psw = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Users {self.id}>'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['psw'])
            new_user = Users(email=request.form['email'], psw=hash)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))
        except:
            db.session.rollback()
            print('Error')
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = Users.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.psw, request.form['psw']):
            login_user(user)
            return redirect(url_for('index'))
        else:
            print("Authorization Error")
    else:
        print("Input Email and Password")
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)
