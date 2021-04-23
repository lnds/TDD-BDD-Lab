from flask import render_template

from models import Book
from main import app

@app.route('/')
def index():
  books = Book.query.all()
  return render_template('index.html', books= books)

@app.route('/detail//<int:book_id>')
def detail(book_id):
  book = Book.query.get(book_id)
  return render_template('detail.html', book=book)