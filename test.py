import unittest
from flask_testing import TestCase
from main import create_app
from models import db, Author
from services import *

class DatabaseTestCase(TestCase):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite://'

  def create_app(self):
   return create_app(self)

  def setUp(self):
    init_db()

  def tearDown(self):
    db.session.remove()
    db.drop_all()


class ServiceTests(DatabaseTestCase):

  def test_author_creation(self):
    author = create_author(name="Homero")
    assert author.id
    assert author.name == "Homero"

  def test_find_book(self):
    book = find_book("Iliada")
    assert book is None
    book = find_book("Hamlet")
    assert book
    assert book.author.name == "William Shakespeare"


  def test_book_creation(self):
    book = create_book(title="Odisea", author_name="Homero", price=1000, stock=100)
    assert book
    assert book.price == 1000
    assert book.stock == 100

  def test_book_purchase(self):
    book = find_book(title="Hamlet")
    assert book
    stock = book.stock
    book = purchase_book(book, 1)
    assert book
    assert book.stock and book.stock < stock
    book = purchase_book(book, stock+1)
    assert book is None


if __name__ == '__main__':
  unittest.main()