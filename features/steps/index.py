from behave import *
from views import *

@given(u'hemos accedido a la aplicación')
def setup(context):
    assert context.client and context.db

@when(u'carguemos la pagina /')
def load_page(context):
    context.page = context.client.get('/', follow_redirects=True)
    assert context.page

@then(u'aparece el título "{title}"')
def check(context, title):
    assert title in context.page.data.decode()

@then(u'aparece el libro {libro}')
def check(context, libro):
    assert libro in context.page.data.decode()