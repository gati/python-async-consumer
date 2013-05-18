import urllib2
import simplejson as json
import logging

from polling_retriever import PollingRetriever

class ExampleRetriever(PollingRetriever):
    url = "http://api.openweathermap.org/data/2.5/weather"
    location = "Austin,TX"
    interval = 60 # seconds

    def retrieve(self):
        url = "%s?q=%s" % (self.url, self.location)
        
        response = urllib2.urlopen(url)
        result = response.read()

        json_result = json.loads(result)

        message = {
            'sender': 'example',
            'data': json_result
        }

        self.result.set(message)