from venv import main
from flask import render_template
from ..requests import get_source, get_articles, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main 



@main.route('/')
def index():


    return render_template()