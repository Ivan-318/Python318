from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase

DEBUG = True
SECRET_KEY = 'c5e4adf5aba5dcaf09f66c73eadf1b153cfc1ee2'

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
    if not hasattr(g, 'link.db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link.db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()



