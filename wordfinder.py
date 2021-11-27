"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Finds random words 

>>> wf = WordFinder("lst.txt")
    3 words read

    >>> wf.random() in ["fish", "bird", "rat"]
    True

    >>> wf.random() in ["fish", "bird", "rat"]
    True

    >>> wf.random() in ["fish", "bird", "rat"]
    True
    """
def __init__(self, path):
        """looks in dictionary and gives # words read."""

        words_in_file = open(path)

        self.words = self.parse(words_in_file)

        print(f"{len(self.words)} words read")
    
     #had to look at solution
    def parse(self, words_in_file):
        """Parse words_in_file -> list of words."""

        return [w.strip() for w in words_in_file]

    def random(self):
        """Makes random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("2nd.txt")
    4 words read

    >>> swf.random() in ["snakes", "turtles", "salamanders", "frogs"]
    True

    >>> swf.random() in ["snakes", "turtles", "salamanders", "frogs"]
    True

    >>> swf.random() in ["snakes", "turtles", "salamanders", "frogs"]
    True

    >>> swf.random() in ["snakes", "turtles", "salamanders", "frogs"]
    True

    """
    #had to look at solution
    def parse(self, words_in_file):
        """Parse words_in_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in words_in_file
                if w.strip() and not w.startswith("#")]
    

