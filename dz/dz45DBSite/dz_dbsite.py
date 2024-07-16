from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase

DEBUG = True
SECRET_KEY = 'f2e64aada083ea18513a45abe7e06d2fe6f3e3eb'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu(), courses=dbase.get_course_annonce())


@app.route("/add_course", methods=["POST", "GET"])
def add_course():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if (len(request.form["course_name"]) > 4 and int(request.form["price"]) > 1000 and
                len(request.form["description"]) > 10):
            res = dbase.add_course(request.form["course_name"], request.form["price"], request.form["description"])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template('add_course.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/course/<int:id_course>")
def show_description(id_course):
    db = get_db()
    dbase = FDataBase(db)

    course_name, price, description = dbase.get_course(id_course)
    return render_template('course.html', menu=dbase.get_menu(), course_name=course_name,
                           price=price, description=description)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()
