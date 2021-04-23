from models import *


class AuthorNotFound(Exception):
  pass

class BookNotFound(Exception):
  pass

  
def create_author(name: str) -> Author:
  return None 

""" 
Find author by name, then create Book
Raise exception if author is not found
"""
def create_book(title: str, author_name: name, price: int, stock: int) -> Book:
  return None

def purchase_book(title: str, cantity: int) -> Book:
  return None  