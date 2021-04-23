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
  imagen = db.Column(db.String(100))

  author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
  author = db.relationship("Author", backref=db.backref("books", lazy=True))


def init_db():
  db.create_all()
  shakespeare = Author(name="William Shakespeare")
  db.session.add(shakespeare)
  cervantes = Author(name="Miguel De Cervantes")
  db.session.add(cervantes)
  hamlet = Book(title="Hamlet", price=2000, stock=10, author=shakespeare, imagen='hamlet.jpg')
  db.session.add(hamlet)
  quijote = Book(title="El Quijote de la Mancha", price=3000, stock=20, author=cervantes, imagen='elquijote.jpg')
  db.session.add(quijote)
  db.session.commit()

if __name__ == "__main__":
  print("Creating database tables")
  init_db()
  