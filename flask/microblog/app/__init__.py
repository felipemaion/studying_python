from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes



# FOLLOWING THE WEB SITE
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database