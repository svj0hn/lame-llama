import sys

class RhymeThyme(object):

    def rhyme_thyme(self, word):
        # Init -- load corpus etc.
        # Look for rhyming word

        # Output rhyming word
        return 'Thyme'

    def input_from_user(self):
        # Input word
        version_info = sys.version_info[:2]
        using_python_v3 = version_info[0] == 3
        out_str = 'Input word:   '
        word = input(out_str) if using_python_v3 else raw_input(out_str)

    def output_to_user(self, word):
        # Output word to user
        print('Rhyming word:  ' + word)

    def print_welcome_text(self):
        print("Welcome to Rhyme Thyme - the awesome rhyming time. \n")

    def __init__(self):
        self.print_welcome_text()
        word = self.input_from_user()
        rhyming_word = self.rhyme_thyme(word)
        self.output_to_user(rhyming_word)

if __name__ == '__main__':
    RhymeThyme()
