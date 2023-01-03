# GoText
GoText is a universal text extraction and preprocessing tool for python which supportss wide variety of document formats (using [Textract-Plus](https://github.com/vaibhavhaswani/textract-plus)).

## Install

```
pip install gotext
```

## How To Use

``` python
from gotext import GoDocument

#process all the documents within a directory
docs_dir='docs/'
go_obj=GoDocument(docs_dir=docs_dir)
print(go_obj.preprocess()) #preprocess documents and returns a list of preprocessed text
```

## Feedback / Queries

For any queries or feedback feel free to write to vaibhavhaswani@gmail.com
