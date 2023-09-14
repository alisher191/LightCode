from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

students = ["Elvira", "Aktilek", "Nurmuhammed", "Meder", "Ulukbek"]

@app.route('/')
def home():
    return render_template('index.html', students=students)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            with open("info.txt", 'w') as f:
                d = [name, password, email]
                for i in d:
                    f.write(str(i)+',')
        except:
            print("Error")

    return render_template("post_temp.html")


@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        try:
            name = request.form['name']
            password = request.form['password']

            with open("info.txt") as f:
                users = f.read()

            users = users.split(",")
            user = {
                'name': users[0],
                'password': users[1],
                'email': users[2]
                }
            if name == user["name"] and str(password) == user['password']:
                return redirect(url_for('home'))
        except:
            print("Error")

    return render_template("temp.html")


if __name__ == '__main__':
    app.run(debug=True)
