import unittest
from unittest.main import main
# from ..app import create_app
# app=create_app('development')
from app.models import Article

class ArticleTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Source 
  '''

  def setUp(self):
    '''
    setUp method that will run 
    '''
    self.new_source=Article('bbc','Bbc','Kevin',"sdafsd","rewrfefde","https://sdfds.com","https://sdfds.com","29/01/2022","fdsfdsfdsfdsfdsf")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Article))

if __name__=='__main__':
  unittest.run()