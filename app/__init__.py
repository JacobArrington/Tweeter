# !!START
from flask import (Flask, render_template)
from .config import Config
# from . import tweets as tweets
# import random 



app = Flask(__name__)

from app import routes

app.config.from_object(Config)


    
