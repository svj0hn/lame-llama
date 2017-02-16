from mockito import mock, verify
import unittest

from rhyme_thyme import rhyme_thyme

class RhymeThymeTest(unittest.TestCase):
    def test_should_issue_default_message(self):
        out = mock()

        rhyme_thyme(out)

        verify(out).write("Thyme\n")
