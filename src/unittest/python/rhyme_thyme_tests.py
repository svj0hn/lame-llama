import unittest

from rhyme_thyme import RhymeThyme

class test_rhyme_thyme(unittest.TestCase):

    def test_output(self):
        print('in output test')
        #self.assertEqual(self.obj.rhyme_thyme(self,''), 'Thyme\n', 'Not equal!')
        #self.assertEqual(RhymeThyme.rhyme_thyme(self,''), 'Yo mama\n', 'Not equal!')

    def test_goodbye(self):
        obj = RhymeThyme()
        self.assertEqual(obj.print_goodbye_text(), 'Goodbye!\n')
    
