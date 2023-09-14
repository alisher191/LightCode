from flask import Flask, render_template

app = Flask(__name__)

menu = ["Блог", "Услуги", "Контакты", "Продукция"]
number = 552405553


@app.route('/')
def index():
    return render_template('index.html', menus=menu, number=number)


if __name__ == '__main__':
    app.run(debug=True)
