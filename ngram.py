from trie import Trie

class Ngram(object):
    def __init__(self, seq:list):
        self.seq = seq

    def build(self, n:int=1) -> Trie:
        trie = Trie()
        for i in range(len(self.seq) + 1 - n):
            tokens = self.seq[i:i+n]
            if '</s>' in tokens[:-1]:
                continue
            if tokens not in trie:
                trie[tokens] = 0
            trie[tokens] += 1

        return trie