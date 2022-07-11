import unittest

from main import tzeva


#class testMain(unittest.TestCase):


#class TestMethods(unittest.TestCase):

 #   def test_ok(self)  :
  #      message  = 'true'
   #     check = 'https:\/\/i.imgflip.com\/30b1gx.jpg'
    #    self.assertisnotNone(check, message)




def test_colors():

    assert tzeva('https://i.imgflip.com/30b1gx.jpg') == [(216, 186, 19), (177, 74, 8), (71, 30, 4), (204, 116, 44)], "should be '[(216, 186, 19), (177, 74, 8), (71, 30, 4), (204, 116, 44)]"




