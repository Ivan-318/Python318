from flask import Flask, render_template, make_response

app = Flask(__name__)

menu = [
    {'name': 'Главная страница', 'url': 'index'},
    {'name': 'Информация о сайте туристического агентства', 'url': 'about'},
    {'name': 'Путеводитель', 'url': 'destinations'},
    {'name': 'Наши контакты', 'url': 'contact'},
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Главная страница", menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title="Информация о сайте", menu=menu)


@app.route('/destinations')
def destinations():
    return render_template('destinations.html', title="Путеводитель", menu=menu)


@app.route('/contact')
def contacts():
    return render_template('contact.html', title="Контакты", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
