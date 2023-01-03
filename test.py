from gotext import GoDocument
from gotext import GoMetrics as gm


#process all the documents within a directory
docs_dir='sample_docs/'
go_obj=GoDocument(docs_dir=docs_dir)
# print(go_obj._text) #returns a list of texts extracted from all the documents
# print(go_obj.preprocess()) #preprocess documents and returns a list of preprocessed text
# print(go_obj.gograms(2))
doc1="i am a go test"
doc2="i am the gotest"
print(gm.cosine_similarity(doc1,doc2))
print(gm.jaccard_similarity(doc1,doc2))
print(gm.wer(doc1,doc2))