from transformers.base_transformer import Transformer

"""
The example below assumes a JSON structure like...

[
    {
        "title":"Whatever",
        "slug":"my-slug"
    },
    {
        "title":"Another Title",
        "slug":"another-slug"
    }
]
"""

class ExampleTransformer(Transformer):
    def __init__(self,data):
        self.data = data
    
    def transform(self):
        return [self.map(item) for device in self.data['items']]

    def map(self,item):
        return {
            'name': data.get('title', None),
            'sluggly': data.get('slug', None)
        }