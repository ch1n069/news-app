from venv import main
from flask import render_template
from ..request import get_source, get_articles, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main 



@main.route('/')
def index():


    sources = get_source()
    # get articles from bbc-news
    bbc_news = get_articles_from_source_selected('bbc-news', '8')
    # get articles from al-jazeera-english



    return render_template()