from flask import render_template
from app import app
from ..requests import get_source, get_articles



@app.route('/')
def index():


    return render_template()