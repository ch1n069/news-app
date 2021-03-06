import os


class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string here it is'



class ProdConfig(Config):
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    


class DevelopmentConfig(Config):
    DEBUG = True


config_map = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}