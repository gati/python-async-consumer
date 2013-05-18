from core.actor import Actor


class Broker(Actor):
    def __init__(self, transformers, publishers):
        super(Broker, self).__init__()
        self.transformers = transformers
        self.publishers = publishers
        self._publishers = {}

    def get_transformer(self, sender):
        return self.transformers.get(sender, None)

    """
    Unlike our transformer, we want to use a single instance of each publisher
    for the life of the application, allowing the publisher to reuse a small
    number of connections to whatever its publishing to if desired
    """
    def get_publisher(self, sender):
        if sender in self._publishers:
            return self._publishers[sender]
        else:
            Publisher = self.publishers.get(sender, None)
            if Publisher:
                self._publishers[sender] = Publisher()
                return self._publishers[sender]
        return None

    def receive(self, message):
        Transformer = self.get_transformer(message['sender'])
        publisher = self.get_publisher(message['sender'])
        if Transformer:
            data = Transformer(message['data']).transform()
            publisher.publish(message['sender'], data)
