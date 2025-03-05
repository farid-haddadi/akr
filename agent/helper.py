import os

class Endpoint:
    def __init__(self, url, **param):
        self.url = url
        self.param = param

    def show(self):
        print(self.url)
        print(self.param)

class Headers:
    def __init__(self):
        self.headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
        self.api_key =  {"api-key": open(os.path.join(os.path.expanduser('.'), ".akr_key.txt"), 'r').read().strip()}

class HttpRequest(Endpoint, Headers): # heritage multiple
    def __init__(self, url, **param):
        Endpoint.__init__(self, url, **param)
        Headers.__init__(self)

    def show(self):
        print(f"show from HttpRequest: {self.url.format(**self.param)}") # gérer les erreur
        print(f"show from HttpRequest: {self.headers}")