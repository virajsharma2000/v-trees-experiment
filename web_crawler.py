from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def web_crawl(links, visited_links = []):
 new_links = []
 
 for link in links:
  try:
   soup = BeautifulSoup(requests.get(link).text, 'html.parser')

   for node in soup.find_all('a'):
     url = urljoin(link, node['href']) 
     
     if url not in visited_links: 
      print(visited_links)
      soup = BeautifulSoup(requests.get(url).text, 'html.parser')
   
      visited_links.append(url)
      
      if soup.find_all('a'):
       new_links.append(url)

  except:
   pass
 
 if new_links:
  return web_crawl(new_links)

 else:
  return visited_links
 


print(web_crawl(['https://www.arunponnusamy.com/']))


