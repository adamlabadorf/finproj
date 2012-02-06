import collections
import csv
import urllib
import sys

YAHOO_QUOTE_URL = "http://finance.yahoo.com/d/quotes.csv?s=%(symbols)s&f=%(tags)s"

def get_symbol_data(symbols,tags='snol1ghvd1') :
    if isinstance(symbols,str) :
        symbols = [symbols]
    url_str = YAHOO_QUOTE_URL%{'symbols':'+'.join(symbols),'tags':tags}
    sys.stderr.write(url_str)
    url_f = urllib.urlopen(url_str)
    recs = []
    for r in csv.reader(url_f) :
        recs.append(r)

    return recs
