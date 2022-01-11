from searchenginebase import SearchEngineBase
import re

class BOWSearchEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_words = {}
    
    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)
    
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True    

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub('[^\w ]', ' ', text)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)
        
    
