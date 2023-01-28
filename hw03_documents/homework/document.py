from nltk.tokenize import word_tokenize
from nltk


def normalized_tokens(text):
    x = word_tokenize(text.lower())
    return x

    # """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    # pass TODO: return list with lower-case tokens.

class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text = text
        self.word_to_count = dict()
        # self.word_to_count = None # TODO: Create dictionary that maps words to their counts.
        # for key in self.text.split():
        #     self.word_to_count[key] = self.word_to_count.get(key,0) +1
        for key in word_tokenize(text.lower()):
            self.word_to_count[key] = self.word_to_count.get(key, 0) + 1
        self.id = id

    @classmethod
    def from_file(cls,filename):
        """ This creates a TextDocument instance by reading a file. """
        text = "" # TODO: read text from filename
        with open(filename,'r',encoding='utf8') as f:
            for readline in f.readlines():
                text += readline
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        if len(self.text) > 25:
            return self.text[:22]+'...'
        return self.text
        # pass # TODO: Implement correct return statement.

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        same_words = set()
        for i in self.text.split():
            for j in other_doc.text.split():
                if i == j:
                    same_words.add(i)
                    continue
        return len(same_words)

        # pass # TODO: Implement correct return statement.

a = TextDocument("the fat cat sat on a mat",'file1')
