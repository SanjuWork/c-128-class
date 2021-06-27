html_doc="""<html>
 <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link3">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
   <p class="story">
    ...
   </p>
  </body>
 </html>"""
 
 ##simple concept by beautifulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#types of objects - tag
"""soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
type(tag)"""

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])

#print(soup.prettify()) ##printing complete html file

#Here are some simple ways to navigate that data structure:
"""print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.p['class'])
print(soup.find(id="link3"))
print(soup.find_all('a'))
print(soup.title.name)"""


#extracting all the URLs found within a page’s <a> tags:
"""for link in soup.find_all('a'):
    print(link.get('href'))

#extracting all the text from a page:
print(soup.get_text())"""