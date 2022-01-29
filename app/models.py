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