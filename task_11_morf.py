import xml.etree.ElementTree as etree


class Corpus:

    def __init__(self):
        self._sentences = []

    def load(self, corpus):
        tree = etree.parse(corpus)
        root = tree.getroot()
        for sentence in root.iter('sentence'):
            self._sentences.append(Sentence(sentence))

    def get_sentence(self, n1):
        if type(n1) == int:
            try:
                return str(self._sentences[n1])
            except IndexError:
                return 'Предложения с запрашиваемым индексом нет в корпусе'

    def get_word(self, n1, n2):
        if type(n1, n2) == int:
            try:
                return str(self._sentences[n1].get_words()[n2])
            except IndexError:
                return 'Предложения и слова с запрашиваемымы индексами нет в корпусе'

    def get_grammem(self, n1, n2, n3):
        if type(n1, n2, n3) == int:
            try:
                return str(self._sentences[n1].get_words()[n2].get_grammems()[n3])
            except IndexError:
                return 'Предложения,слова и граммемы с запрашиваемымм индексами нет в корпусе'

    def show_info(self, n1):
        if type(n1) == int:
            try:
                word_gram = []
                for word in self._sentences[n1].get_words():
                    word_gram.append((str(word), word.get_grammems()))
                return f'Предложение: \n  "{str(self._sentences[n1])}";\n'\
                       f'Слова и граммемы: \n "{word_gram[0]},{word_gram[1]}'
            except IndexError:
                return 'Предложения с запрашиваемым индексом нет в корпусе'


class Sentence:
    def __init__(self, wordforms):
        self._wordforms = wordforms
        for token in wordforms.iter('token'):
            is_word = True
            for g in token.iter('g'):
                if g.get('v') == 'PNCT':
                    is_word = False
            if is_word:
                self._wordforms.append(WordForm(token))
        self._strsent = wordforms.find('source').text

    def get_words(self):
        return self._wordforms

    def __str__(self):
        return self._strsent


class WordForm:
    def __init__(self, token):
        self._grammems = []
        self._strword = token.get('text').lower()
        for g in token.iter('g'):
            self._grammems.append(g.get('v'))

    def get_grammems(self):
        return self._grammems

    def __str__(self):
        return self._strword


corp = Corpus()
corp.load('annot.opcorpora.no_ambig.xml')

print(corp.show_info(20))
print(corp.get_word(20, 1))
print(corp.get_grammem(20, 1, 1))
print(corp.get_sentence(22))
