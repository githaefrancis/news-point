from ast import parse
from datetime import datetime
from pydoc import describe
import urllib.request,json
from .models import Source,Article
from dateutil.parser import isoparse
from dateutil.tz import UTC

api_key=None
base_url=None

def configure_request(app):
  global api_key,base_url
  api_key=app.config['NEWS_API_KEY']
  base_url=app.config['NEWS_BASE_URL']

def get_sources():
  '''
  Function that gets the json response for the get sources request 
  '''
  get_sources_url=f"{base_url}top-headlines/sources?apiKey={api_key}"

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data=url.read()
    get_sources_response=json.loads(get_sources_data)
    sources_results=None

    if get_sources_response['sources']:
      sources_result_list=get_sources_response['sources']
      sources_results=map_sources_results(sources_result_list)
  print("HELLO")
  return sources_results 

def get_headlines():
  '''
  Function that gets the json response for the headline articles
  '''
  get_headlines_url=f"{base_url}top-headlines?country=us&apiKey={api_key}"
  with urllib.request.urlopen(get_headlines_url) as url:
    get_headlines=url.read()
    get_headlines_response=json.loads(get_headlines)
    headlines_results=None

    if get_headlines_response['articles']:
      headlines_result_list=get_headlines_response['articles']
      headlines_results=map_articles_results(headlines_result_list)
  return headlines_results

def get_news_from_source(source_id):
  get_news_url=f"{base_url}everything?sources={source_id}&apiKey={api_key}"
  with urllib.request.urlopen(get_news_url) as url:
    get_news=url.read()
    get_news_response=json.loads(get_news)
    news_results=None

    if get_news_response['articles']:
      news_results_list=get_news_response['articles']
      news_results=map_articles_results(news_results_list)


  return news_results

def get_category_news(category):
  get_category_news_url=f"{base_url}top-headlines?category={category}&apiKey={api_key}"
  with urllib.request.urlopen(get_category_news_url) as url:
    get_category_news=url.read()
    get_category_news_response=json.loads(get_category_news)
    category_news_results=None

    if get_category_news_response['articles']:
      category_news_list=get_category_news_response['articles']
      category_news_results=map_articles_results(category_news_list)

  return category_news_results
  
def map_sources_results(sources_results):
  '''
  map_results function to create sources objects
  
  Args:
      A list of sources response

  Returns:
        A list of sources objects
  '''

  sources_list=[]
  for source in sources_results:
    id=source.get('id')
    name=source.get('name')
    description=source.get('description')
    url=source.get('url')
    category=source.get('category')
    country=source.get('country')
    print(name)
    new_source=Source(id,name,description,url,category,country)
    sources_list.append(new_source)

  return sources_list

def map_articles_results(headlines_results):
  '''
  map articles results to a list of article objects

  Args:
      List of articles from the payload

  Returns:
        A list of articles objects
  '''
  headlines_list=[]
  for headline in headlines_results:
    source_id=headline.get('source').get('id')
    source_name=headline.get('source').get('name')
    author=headline.get('author')
    title=headline.get('title')
    description=headline.get('description')
    url=headline.get('url')
    image_url=headline.get('urlToImage')
    publication_date=headline.get('publishedAt')
    content=headline.get('content')
    pub_date=isoparse(publication_date)
    pub_date.astimezone(UTC)
    converted_publication_date=pub_date.strftime("%b %d, %Y %H:%M:%S")
    
    if content:
      headline_object=Article(source_id,source_name,author,title,description,url,image_url,converted_publication_date,content)
      headlines_list.append(headline_object)

  return headlines_list