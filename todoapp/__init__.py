from flask import Flask
from flask_login import LoginManager
from peewee import PostgresqlDatabase
from flask_bcrypt import Bcrypt

from os import environ
from urllib.parse import urlparse

app = Flask(__name__)
key = environ.get('TodoAppSecretKey', None)
if not key:
    raise Exception('no secret key set'
                    'please set TodoAppSecretKey '
                    'environmental variable')
app.secret_key = key

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port
db = PostgresqlDatabase(dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

lm = LoginManager()
lm.init_app(app)
crypt = Bcrypt(app)
from todoapp import routes
