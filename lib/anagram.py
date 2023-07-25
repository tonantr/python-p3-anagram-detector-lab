
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []
        for i in words:
            if sorted(i.lower()) == sorted(self.word.lower()):
                matches.append(i)

        return matches

