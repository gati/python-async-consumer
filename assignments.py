from transformers import example
from retrievers import example as r_example
from publishers import example as p_example

"""
As messages moved through the system they is identified by a "key" property, 
assigned in the retriever, which we use to determine which transformer and 
publisher to use for that message. 
"""

transformers = {
  "example": example.ExampleTransformer
}

publishers = {
  "example": p_example.ExamplePublisher 
}

"""
The retrievers that should be instantiated and run when the process is started.
"""
retrievers = [
  example.ExampleRetriever,
]
