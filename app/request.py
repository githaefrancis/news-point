import urllib.request,json
from .models import Source

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
      sources_results=map_results(sources_result_list)

  return sources_results 


def map_results(sources_results):
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

    new_source=Source(id,name,description,url,category,country)
    sources_list.append(new_source)

  return sources_list