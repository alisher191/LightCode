from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        if len(pass1) >= 8 and len(pass1) <= 16:
            if pass1 == pass2:
                print('Успех!')
            else:
                print('Passwords no equal')
        else:
            print('Error!')

    return render_template('index.html')

@app.route('/second')
def second():
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)