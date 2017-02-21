import unittest

from rhyme_thyme import RhymeThyme

class test_rhyme_thyme(unittest.TestCase):

    def test_output(self):
        #self.assertEqual(RhymeThyme.rhyme_thyme(self), 'Thyme\n', 'Not equal!')
        self.assertEqual(RhymeThyme.rhyme_thyme(self), 'Yo mama\n', 'Not equal!')



#import unittest

##from rhyme_thyme import rhyme_thyme

#def rhyme_thyme():
#    return "Thyme\n"

#class test_rhyme_thyme(unittest.TestCase):

#    def test_output(self):
#        self.assertEqual(rhyme_thyme(), 'Thyme\n', 'not equal ')
#        #self.assertEqual(rhyme_thyme(), 'Yo mama', 'not equal ') # not correct behaviour


#if __name__ == '__main__':
#    #print(rhyme_thyme()) ## 
    
   
#    unittest.main()
	
	
#from mockito import mock, verify
#import unittest

#from rhyme_thyme import rhyme_thyme

#class RhymeThymeTest(unittest.TestCase):
#    def test_should_issue_default_message(self):
#        out = mock()

#        rhyme_thyme(out)

#        verify(out).write("Thyme\n")