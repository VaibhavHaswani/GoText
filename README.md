# GoText v0.9
GoText is a universal text extraction and preprocessing tool for python which supports wide variety of document formats (using [Textract-Plus](https://github.com/vaibhavhaswani/textract-plus)).

## Install

```
pip install gotext
```

## How To Use

``` python
from gotext import GoDocument

# process single document
doc_path='docs/test.docx'
go_obj=GoDocument(doc_path=doc_path)
print(go_obj._text) #returns text extracted from document
print(go_obj.preprocess()) #preprocess document and returns preprocessed text

#process all the documents within a directory
docs_dir='docs/'
go_obj=GoDocument(docs_dir=docs_dir)
print(go_obj._text) #returns a list of texts extracted from all the documents
print(go_obj.preprocess()) #preprocess documents and returns a list of preprocessed text
```

## Feedback / Queries

For any queries or feedback feel free to write to vaibhavhaswani@gmail.com
