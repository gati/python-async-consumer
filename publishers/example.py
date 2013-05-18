from publishers.publisher import Publisher

"""
Here you'd ping a client with the transformed data, write to a datastore, 
etc.
"""

class ExamplePublisher(Publisher):
    def publish(self, sender, message):
        print message

