import requests

class Loader:
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        pass

    def load_page(self, url):
        # load and return the response object which will hit various parsers, each with their own purpose
        response = requests.get(url, headers=self.headers)

        return response