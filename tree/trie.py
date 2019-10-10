class Trie:
    def __init__(self):
        self.prefix_tree = {}

    def add(self, new_word):
        curr_pfxs = self.prefix_tree

        for char in new_word:
            if char not in curr_pfxs:
                curr_pfxs[char] = {}
            curr_pfxs = curr_pfxs[char]

    def get_words_with_prefix(self, prefix):
        curr_pfxs = self.prefix_tree

        for char in prefix:
            curr_pfxs = curr_pfxs[char]
            if not curr_pfxs:
                return set()

        def _get_words(prefix, next_map=curr_pfxs, found=set()):
            for next_char, following in next_map.items():
                curr_pfx = prefix + next_char
                if not following:
                    found.add(curr_pfx)
                else:
                    _get_words(curr_pfx, following, found)
            return found

        return _get_words(prefix)

if __name__ == '__main__':
    with open('../english-words/words_alpha.txt') as words:
        trie = Trie()
        word = words.readline().strip()
        while word:
            trie.add(word)
            word = words.readline().strip()

        while True:
            pfx = input('Prefix: ')
            print(trie.get_words_with_prefix(pfx))

