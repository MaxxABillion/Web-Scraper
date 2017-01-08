import bs4 as bs
import urllib.request

source = urllib.request.urlopen ('http://finviz.com/screener.ashx?v=340&s=ta_topgainers')
soup = bs.BeautifulSoup(source, "html.parser")


print (soup("quote.ashx?t"))