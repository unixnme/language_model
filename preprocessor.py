import os.path as osp

class Tokenizer(object):
    ascii_a = ord('a')
    ascii_z = ord('z')

    '''
    concat sequences with <s> and </s> added for each sentence
    '''
    def __init__(self):
        self.sequence = []

    def tokenize(self, content:str):
        '''
        tokenize given context
        at least one newline for each sentence
        '''
        lines = content.split('\n')
        for line in lines:
            tokens = line.split()
            if not tokens: continue

            self.process_first_token()
            for token in tokens:
                self.process_token(token)
            self.process_last_token()

    def process_last_token(self):
        '''
        process the last token, which has the period at the end
        '''
        self.sequence.append('</s>')

    def process_first_token(self):
        '''
        process the first token
        '''
        self.sequence.append('<s>')

    def process_token(self, token:str):
        raw_token = token.lower()
        token = ''

        for c in raw_token:
            if self.ascii_a <= ord(c) <= self.ascii_z:
                token += c
        if token:
            self.sequence.append(token)


class Preprocessor(object):
    def __init__(self, corpus_list:str):
        '''
        given a file that contains the list of all raw text corpus,
        it will return the preprocessor instance
        '''
        assert osp.isfile(corpus_list), '%s does not exist' % corpus_list
        self.corpus_files = []
        with open(corpus_list, 'r') as f:
            for line in f:
                assert len(line.split()) == 1, 's is not a valid filename' % line
                self.corpus_files.append(line.split()[0])
        self.tokenizer = Tokenizer()

    def tokenize(self):
        for filename in self.corpus_files:
            with open(filename, 'r') as f:
                self.tokenizer.tokenize(f.read())

