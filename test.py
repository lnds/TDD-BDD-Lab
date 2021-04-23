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
    db.create_all

  def tearDown(self):
    db.session.remove()
    db.drop_all()


class ServiceTests(DatabaseTestCase):

  def test_author_creation(self):
    author = create_author(name="Homero")
    assert author.id > 0

  def test_book_creation(self):
    author = create_book(name="Homero")
    assert author.id > 0

  def test_book_purchase(self):
    author = create_author(name="Homero")
    assert author.id > 0


if __name__ == '__main__':
  unittest.main()