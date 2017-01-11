import unittest 
from bangazon import *

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class Test_Human_Resources(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.HR = Human_Resources("Human Resources", "Bob", 2)


  @classmethod
  def tearDownClass(self):
    print('Tear down class')



  def test_HR_is_a_Department(self):
    self.assertIsInstance(self.HR, Department)
  	

  def test_get_name(self):
  	self.assertEqual(self.HR.get_name(), "Human Resources")


  def test_get_supervisor(self):
  	self.assertEqual(self.HR.get_supervisor(), "Bob")


  def test_get_size(self):
  	self.assertEqual(self.HR.get_size(), 2)

  



  

if __name__ == '__main__':
    unittest.main()
