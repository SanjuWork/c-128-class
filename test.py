from bs4 import BeautifulSoup
import urllib.request

html_page = urllib.request.urlopen("https://exoplanets.nasa.gov/discovery/exoplanet-catalog/")
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a'):
    print(link.get('href'))
    
    