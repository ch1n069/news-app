from urllib.request
import json
from .models import Sources,Articles


api_key = ''


base_url_source = None


base_url_articles = None


def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_API_SOURCE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']



