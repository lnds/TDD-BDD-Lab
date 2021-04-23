from models import *
from typing import Optional

"""
  Return None if book not found
"""
def find_book(title: str) -> Optional[Book]:
  return Book()

"""
If author already exists return author from database
"""
def create_author(name: str) -> Author:
  author = Author(name=name)
  return author

""" 
Find author by name, then create Book
Return None if author not found
If book already exists return that book
"""
def create_book(title: str, author_name: str, price: int, stock: int) -> Optional[Book]:
  return Book()


"""
If cantity > stock return None
"""
def purchase_book(book: Book, quantity: int) -> Optional[Book]:
  return Book()