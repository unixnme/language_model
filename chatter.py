from trie import Trie
import numpy as np

class Chatter(object):
    def __init__(self, tries:list):
        '''
        tries should be [unigram, bigram, trigram, ...] in the order
        '''
        self.N = len(tries)
        self.ngrams = tries

    def chat(self):
        '''
        generate random sentence from n-grams
        '''

        tokens = ['<s>']
        while tokens[-1] != '</s>':
            tks = tokens[-self.N + 1:]
            N = len(tks)
            while tks not in self.ngrams[N]:
                N -= 1
                tks = tks[-1:]

            next_token = self.random_token(self.ngrams[N][tks])
            tokens.append(next_token)

            '''
            idx = np.asarray([tokens[-self.N+1:] in ngram for ngram in self.ngrams]).sum()
            for i in reversed(range(idx+1)):
                next_token = self.random_token(self.ngrams[i][tokens[-i:]])
                if next_token:
                    tokens.append(next_token)
                    break
            '''

        return ' '.join(tokens)


    @staticmethod
    def random_token(trie:Trie):
        N = len(trie.data)
        keys = np.empty((N,), dtype=object)
        counter = np.empty((N,), dtype=np.int64)

        idx = 0
        for key,count in trie.data.items():
            if isinstance(count, int):
                keys[idx] = key
                counter[idx] = count
                idx += 1

        if idx == 0:
            return None

        keys = keys[:idx]
        counter = counter[:idx]

        cumsum = np.cumsum(counter)
        r = np.random.randint(cumsum[-1])
        idx = (cumsum <= r).sum()

        return keys[idx]
