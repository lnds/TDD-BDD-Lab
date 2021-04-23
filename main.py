from flask import Flask

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
  
if __name__ == "__main__":
  from views import *
  app.run(host='0.0.0.0', port=8080)