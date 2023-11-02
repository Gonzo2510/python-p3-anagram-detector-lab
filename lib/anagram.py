class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matching_items = []
        for item in list:
            if sorted(self.word) == (sorted(item)):
                matching_items.append(item)
        return matching_items




# Anagram('listen').match(['enlists', 'google', 'inlets', 'banana'])