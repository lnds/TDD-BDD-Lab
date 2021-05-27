from flask import Flask
from flask import render_template

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)
  from models import db
  db.init_app(app)
  return app

class Config:
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'

app = create_app(Config())

from models import Book

@app.route('/')
def index():
  books = Book.query.all()
  return render_template('index.html', books= books)

@app.route('/detail//<int:book_id>')
def detail(book_id):
  book = Book.query.get(book_id)
  return render_template('detail.html', book=book)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
