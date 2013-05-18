import gevent.monkey
gevent.monkey.patch_socket()

import gevent
from gevent.event import AsyncResult

"""
Base class for retrievers that poll HTTP endpoints. It runs forever, making
requests at whatever interval is provided by the sub class. Retrieve method
is responsible for setting the value of the self.result deferred object
created in retrieve_publish.
"""

class PollingRetriever:
    interval = 10 # default to 10 seconds

    def __init__(self, broker):
        self.broker = broker

    def retrieve(self):
        """
        Define in your subclass. Make sure to set self.result with whatever
        is returned by the API you're polling.
        """
        raise NotImplemented()

    def retrieve_publish(self):
        while True:
            self.result = AsyncResult()
            gevent.spawn(self.retrieve)
            self.broker.inbox.put(self.result.get())
            gevent.sleep(self.interval)  
        
    def start(self):
        gevent.spawn(self.retrieve_publish)