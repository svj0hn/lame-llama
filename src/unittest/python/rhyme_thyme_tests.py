import unittest

from rhyme_thyme import RhymeThyme

class test_rhyme_thyme(unittest.TestCase):

    def test_output(self):
        self.assertEqual(RhymeThyme.rhyme_thyme(self,''), 'Thyme\n', 'Not equal!')
        #self.assertEqual(RhymeThyme.rhyme_thyme(self), 'Yo mama\n', 'Not equal!')