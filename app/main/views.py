import re
from flask import render_template
from ..request import get_sources ,get_articles
# get_articles, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main



@main.route('/')
def index():


    sources = get_sources()
   
    title = 'Home - Welcome to News App '
    return render_template('index.html',sources=sources)


@main.route('/articles/<source_id>')
def articles(source_id):

   articles = get_articles(source_id)

   return render_template('health.html', articles=articles)










                                                                                                                                                                                                                                                                                                                                             