from flask import render_template
from ..request import get_sources ,get_articles,get_headlines,get_top
# get_articles, get_articles_from_source_selected, get_articles_depending_on_category_of_the_source
from . import main



@main.route('/')
def index():


    headlines = get_headlines()


    top = get_top()


   
    title = 'Home - Welcome to News App '
    return render_template('index.html',headlines=headlines,top=top)


@main.route('/articles')
def articles():

   articles = get_articles()

   return render_template('articles.html', articles=articles)




@main.route('/sources')
def sources():

   sources = get_sources()

   return render_template('sources.html', sources=sources)














                                                                                                                                                                                                                                                                                                                                             