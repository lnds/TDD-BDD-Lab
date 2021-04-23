from main import app, db

def before_feature(context, feature):
  context.db = db
  app.testing = True
  context.client = app.test_client()


def after_feature(context, feature):
  pass