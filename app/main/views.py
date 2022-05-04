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
    aljazeera = get_articles_from_source_selected('al-jazeera-english', '8')
    cnn_home = get_articles_from_source_selected('cnn', '1')
    bbc_news_home = get_articles_from_source_selected('bbc-news', '2')
    cbc_news = get_articles_from_source_selected('cbc-news', '2')
    title = 'Home - Welcome to News App '
    return render_template('index.html',
                           title=title,
                           bcc=bbc_news_home,
                           bbc_news=bbc_news,
                           cnn_home=cnn_home,
                           sources=sources,
                           cbc_news=cbc_news,
                           aljazeera=aljazeera,
                           )



