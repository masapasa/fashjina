from jina.clients import Client

client = Client(host='http://localhost:8080')

from docarray import DocumentArray

da = DocumentArray.pull('demo-da-images-jina', show_progress=True)

da_query = da[0:1]  # one document for query
da_index = da[1:]  # the rest is for indexing

indexed_docs = client.index(inputs=da_index)
print(f'Indexed Documents: {len(indexed_docs)}')