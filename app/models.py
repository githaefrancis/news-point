class Source:
  '''
  Source class to define news source objects
  
  '''
  def __init__(self,id,name,description,url,category,country):
    self.id=id
    self.name=name
    self.description=description
    self.url=url
    self.category=category
    self.country=country

  def __str__(self):
    return f"{self.id} {self.name}"

class Article:
  '''
  Article class that defines news article objects
  '''
  def __init__(self, source_name,author,title,description,url,image_url,publication_date,content):
    self.source_name=source_name
    self.author=author
    self.title=title
    self.description=description
    self.url=url
    self.image_url=image_url
    self.publication_date=publication_date
    self.content=content
    