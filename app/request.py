import urllib.request
import json
from .models import Sources,Articles


api_key = None


base_url_source = None


base_url_articles = None


def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_SOURCE_URL']
    NEWS_ARTICLES_URL = app.config['NEWS_ARTICLES_URL']    
    # base_url_articles
    api_key =app.config['NEWS_API_KEY']





def get_sources():  # get all sources from the news api
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = 'https://newsapi.org/v2/sources?apiKey=cae08cf647104f67ba2f3b6a8c539dd9'

    with urllib.request.urlopen(get_source_url) as home:
        get_source_data = home.read()
        get_source_response = json.loads(get_source_data)
 
        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results_sources(source_results_list)

    return source_results



def process_results_sources(source_list):

    '''
    Function that processes the source list result and transform them to a list of Objects
'''
    source_result_list = []
    for source_item in source_list:

        id = source_item['id']
        name = source_item['name']
        description = source_item['description']
        url = source_item['url']
        category = source_item['category']
        language = source_item['language'] 


        if url :
            
            source_object = Sources( id, name, description, url, category, language)
            source_result_list.append(source_object)

    return source_result_list





def get_articles():
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_articles_url = 'https://newsapi.org/v2/everything?q=us&from=2022-04-12&language=en&apiKey=cae08cf647104f67ba2f3b6a8c539dd9'
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results



def get_headlines():
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?q=us&language=en&apiKey=cae08cf647104f67ba2f3b6a8c539dd9'
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_results_headlines(headlines_results_list)
    return headlines_results






def get_top():
    '''function to display the top sources'''
    get_top_url = 'https://newsapi.org/v2/everything?q=apple&from=2022-05-04&to=2022-05-04&sortBy=popularity&apiKey=cae08cf647104f67ba2f3b6a8c539dd9'
    with urllib.request.urlopen(get_top_url) as url:
        get_top_data = url.read()
        get_top_response = json.loads(get_top_data)

        headlines_results = None

        if get_top_response['articles']:
            top_results_list = get_top_response['articles']
            top_results = process_results_top(top_results_list)
    return top_results



def process_results_top(top_list):
    '''
        Function that processes the articles list result and transform them to a list of Objects
    '''
    top_results = []
    for top_item in top_list:
        author = top_item.get('author')
        title = top_item.get('title')

        description = top_item.get('description')
        url = top_item.get('url')
        urlToImage = top_item.get('urlToImage')
        publishedAt = top_item.get('publishedAt')
        content = top_item.get('content')

        
        top_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
        top_results.append(top_object)

    return top_results






def process_results_headlines(headlines_list):
    '''
        Function that processes the articles list result and transform them to a list of Objects
    '''
    headlines_results = []
    for headline_item in headlines_list:
        author = headline_item.get('author')
        title = headline_item.get('title')

        description = headline_item.get('description')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        publishedAt =headline_item.get('publishedAt')
        content = headline_item.get('content')

        
        headline_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
        headlines_results.append(headline_object)

    return headlines_results

def process_results_articles(articles_list):
    '''
        Function that processes the articles list result and transform them to a list of Objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')

        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        
        articles_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
        articles_results.append(articles_object)

    return articles_results


# def get_articles_from_source_selected(source, pageLimitSize):
#     '''
#     Function that gets the json response to our url request using the source id and page size
#     '''
#     get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}&pageSize={}'.format(source,
#                                                                                                       api_key, pageLimitSize)
#     with urllib.request.urlopen(get_articles_url) as url:
#         get_articles_data = url.read()
#         get_articles_response = json.loads(get_articles_data)

#         articles_results = None

#         if get_articles_response['articles']:
#             articles_results_list = get_articles_response['articles']
#             articles_results = process_results_articles(articles_results_list)
#     return articles_results


# def get_articles_depending_on_category_of_the_source(category):
#     '''
#     Function that gets the json response to our url request using the category 
#     '''
#     get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(
#         category, api_key)
#     with urllib.request.urlopen(get_articles_url) as url:
#         get_articles_data = url.read()
#         get_articles_response = json.loads(get_articles_data)

#         articles_results = None

#         if get_articles_response['articles']:
#             articles_results_list = get_articles_response['articles']
#             articles_results = process_results_articles(articles_results_list)
#     return articles_results




