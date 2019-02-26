# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("li p a")
#
matchedlinks=root.cssselect("li p a")
#print(matchedlinks)


 
record={}
for link in matchedlinks[0:300]:
  list=link.text_content()
  print(list.encode('utf-8'))
