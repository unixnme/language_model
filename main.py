from preprocessor import Preprocessor
from ngram import Ngram
import pickle
from chatter import Chatter

LOAD_PREPROCESSOR = True
LOAD_UNIGRAM = True
LOAD_BIGRAM = True
LOAD_TRIGRAM = True

if not LOAD_PREPROCESSOR:
    preprocessor = Preprocessor('/home/ykang7/Downloads/OANC-GrAF/corpus_list.txt')
    with open('preprocessor.p', 'wb') as f:
        pickle.dump(preprocessor, f)

else:
    with open('preprocessor.p', 'rb') as f:
        preprocessor = pickle.load(f)

ngram = Ngram(preprocessor.tokenizer.sequence)

if not LOAD_UNIGRAM:
    unigram_trie = ngram.build(1)
    with open('unigram.p', 'wb') as f:
        pickle.dump(unigram_trie, f)
else:
    with open('unigram.p', 'rb') as f:
        unigram_trie = pickle.load(f)

if not LOAD_BIGRAM:
    bigram_trie = ngram.build(2)
    with open('bigram.p', 'wb') as f:
        pickle.dump(bigram_trie, f)
else:
    with open('bigram.p', 'rb') as f:
        bigram_trie = pickle.load(f)

if not LOAD_TRIGRAM:
    trigram_trie = ngram.build(3)
    with open('trigram.p', 'wb') as f:
        pickle.dump(trigram_trie, f)
else:
    with open('trigram.p', 'rb') as f:
        trigram_trie = pickle.load(f)

chatter = Chatter([unigram_trie, bigram_trie, trigram_trie])
for _ in range(100):
    print(chatter.chat())