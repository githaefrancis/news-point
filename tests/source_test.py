import unittest
from unittest.main import main
from ..app import create_app
app=create_app('development')
from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Source 
  '''

  def setUp(self):
    '''
    setUp method that will run 
    '''
    self.new_source=Source(1,'Bbc','British News Source',"https://sdfds.com","Sports","Kenya")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Source))

if __name__=='__main__':
  unittest.main()