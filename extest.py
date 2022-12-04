from jina import Flow
from docarray import Document, DocumentArray

f = Flow().add(uses='jinahub+sandbox://FashionSearchPreprocessor/latest')

with f:
    r = f.post('/', inputs=DocumentArray([Document(text='hello')]))
    print(r.to_json())