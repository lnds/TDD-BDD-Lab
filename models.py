from main import db

Base = db.Model

class Author(Base):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))


class Book(Base):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  price = db.Column(db.Integer)
  stock = db.Column(db.Integer)

  author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
  author = db.relationship("Author", backref=db.backref("books", lazy=True))


if __name__ == "__main__":
  print("Creating database tables")
  db.create_all()