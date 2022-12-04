from operator import index
from jina import Client, Flow
from docarray import DocumentArray, Document
from helper import process_docs, print_results
from config import MAX_DOCS, CSV_FILE, CLOUD_HOST
import click

# flow = Flow.load_config("flow.yml")

flow = (
    Flow(port=12345)
    .add(
        uses="jinahub://FashionSearchPreprocessor/latest",
        uses_with={
            "data_dir": "../data/images/",
            "tensor_shape": (80, 60),
            "rating_range": (0, 5),
            "price_range": (0, 200),
        },
        install_requirements=True,
    )
with flow:
    flow.index