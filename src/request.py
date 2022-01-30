import requests

class Request:

    def __init__(self, url, params):
        self._url = url
        self._params = params
        self._response = None

    def response(self):
        if self._response == None:
            self._response = requests.get(url=self._url, params=self._params)
        
        return self._response