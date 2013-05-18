import assignments
from connector.broker import Broker

"""
Entry point for the web service. Takes dicts of publishers, transformers and
retrievers defined in assignments module, instantiates the Broker and starts 
the retrieval process.
"""


class App:
    def __init__(self):
        self.transformers = assignments.transformers
        self.retrievers = assignments.retrievers
        self.publishers = assignments.publishers

    def start(self):
        self.broker = Broker(self.transformers, self.publishers)
        self.broker.start()

        self.start_retrievers()
        self.broker.get()

    def start_retrievers(self):
        for retriever in self.retrievers:
            r = retriever(self.broker)
            r.start()

app = App()
app.start()
