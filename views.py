from flask import render_template

from models import Book
from main import app

@app.route('/')
def index():
  books = Book.query.all()
  return render_template('index.html', books= books)