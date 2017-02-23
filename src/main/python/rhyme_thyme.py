class RhymeThyme(object):

    def rhyme_thyme(self, word):
        # Init -- load corpus etc.
        # Look for rhyming word

        # Output rhyming word
        return 'Thyme\n'

    def input_from_user(self):
        # Input word
        word = input('Input word:   ')
        return word

    def output_to_user(self, word):
        # Output word to user
        print('Rhyming word:  ' + word)

    def __init__(self):
        word = self.input_from_user()
        rhyming_word = self.rhyme_thyme(word)
        self.output_to_user(rhyming_word)

if __name__ == '__main__':
    RhymeThyme()