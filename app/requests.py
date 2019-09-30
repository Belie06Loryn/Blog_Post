import urllib.request,json
from .models import Quotes


base_quote_url = None

def configure_request(app):
    global base_quote_url
    base_quote_url = app.config['QUOTES_API_BASE_URL']

def getQuotes():
    quotes_object = None
    with urllib.request.urlopen(base_quote_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        

        if get_quotes_response:
            quote = get_quotes_response.get('quote')
            author = get_quotes_response.get('author')
            quotes_object = Quotes(quote,author)

    return quotes_object

  