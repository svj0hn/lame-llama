import sys

class RhymeThyme(object):

    def rhyme_thyme(self, word):
        # Init -- load corpus etc.
        # Look for rhyming word

        # Output rhyming word
        return 'Thyme\n'

    def input_from_user(self):
        # Input word
        version_info = sys.version_info[:2]
        using_python_v3 = version_info[0] == 3
        out_str = 'Input word:   '
        word = input(out_str) if using_python_v3 else raw_input(out_str)
        return word

    def output_to_user(self, word):
        # Output word to user
        text = 'Rhyming word:  ' + word
        print(text)
        return text

    def print_welcome_text(self):
        text = "Welcome to Rhyme Thyme - the awesome rhyming time. \n"
        print(text)
        return text

    def print_goodbye_text(self):
        text = "Goodbye!\n" 
        print(text)
        return text

    def __init__(self):
        self.print_welcome_text()
        word = self.input_from_user()
        rhyming_word = self.rhyme_thyme(word)
        self.output_to_user(rhyming_word)

if __name__ == '__main__':
    RhymeThyme()
