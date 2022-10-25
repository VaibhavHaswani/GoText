import os
from mimetypes import init
import textractplus as tp
from .stopwords import stop_words
import re
import math
from collections import Counter



class GoDocument:
    """GoText Document Constructor
       
       arguments-

       doc_path : specify document path incase of single document
       docs_dir : specify documents directory incase of multiple documents in a directory

       attributes-

       _supported: returns list of all the supported document formats
       _docs: returns list of documents path
       _text: returns extacted text of documents
       _preprocessed: returns list of preprocessed text, constructed after .preprocess() method call

       methods- 

       preprocess() : preprocess the extracted text and returns a list of preprocessed text
       preprocess(stopwords=True) : preprocess the extracted text as well as remove the stopwords and returns a list of preprocessed text
    """

    _supported=["doc" , "docx" , "dot" , "dotx" , "docm" , "pdf", "pptx" , "pptm" , "txt"]
    _stop_words=stop_words

    def __init__(self,doc_path=None,docs_dir=None) -> None:
        if doc_path and docs_dir:
            raise Exception("GoConstructorError: Please Specify only one argument. (doc_path or docs_dir)")
        if doc_path:
            self._docs=[doc_path]
            self._text=[self._extract(doc_path)]
        if docs_dir:
            self._docs=list(map(lambda f:os.path.join(docs_dir,f),os.listdir(docs_dir)))
            self._text=list(map(self._extract,self._docs))
        
    def _extract(self,doc_path):
        if not os.path.isfile(doc_path):
                raise Exception("FileError: Specified path is not a file.")
        return tp.process(doc_path).decode('utf-8')

    def _clean(self,text):
        """cleans the document"""
        text=text.lower()
        text=re.sub("''"," ",text) 
        text=re.sub(r'[0-9]', ' ', text)
        text=re.sub("_"," ",text)
        text=re.sub("(\\W)+"," ",text)
        text=re.sub('(\\b[a-z] \\b|\\b [a-z]\\b)','',text)
        return text

    def _remove_stopword(self,text):
        text_tokens=text.split(' ')
        for w in self._stop_words:
            if w in text_tokens:
                text_tokens = list(filter((w).__ne__, text_tokens))
        return " ".join(list(filter(lambda val:len(val)>3, text_tokens)))

    def preprocess(self,stopwords=False):
        """preprocess the godocument"""
        self._preprocessed=list(map(self._clean,self._text))
        if stopwords:
            self._preprocessed=list(map(self._remove_stopword,self._preprocessed))
        return self._preprocessed



class GoMetrics:

    @staticmethod
    def jaccard_similarity(text_a,text_b):
        '''returns the Jaccard Similarity score of two texts'''
        words_doc1 = set(text_a.lower().split()) 
        words_doc2 = set(text_b.lower().split())
        # Find the intersection of words list of text A & text B
        intersection = words_doc1.intersection(words_doc2)

        # Find the union of words list of text a & text b
        union = words_doc1.union(words_doc2)
            
        return float(len(intersection)) / len(union)

    @staticmethod
    def cosine_similarity(text_a,text_b):
        "returns Cosine Similarity score of two texts"
        vector1 = GoMetrics.text_to_vector(text_a)
        vector2 = GoMetrics.text_to_vector(text_b)

        cosine = GoMetrics.get_cosine(vector1, vector2)
        return cosine

    @staticmethod
    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
        sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
            
    @staticmethod
    def text_to_vector(text):
        WORD = re.compile(r"\w+")
        words = WORD.findall(text)
        return Counter(words)
        

        