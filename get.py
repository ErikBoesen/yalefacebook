import requests
from bs4 import BeautifulSoup

r = requests.get('https://students.yale.edu/facebook/PhotoPageNew',
                 headers={
                     'Cookie': 'JSESSIONID=40F7C9727225DB92A2BA243D11921A44; __cfduid=d3e64860ff3a21bc0bce6269c2614af8a1565532230; _ga=GA1.2.2025653848.1578368543',
                 },
                 params={
                     # Load all
                     'currentIndex': -1,
                     'numberToGet': -1,
                 })

bs = BeautifulSoup(r.text, 'html.parser')

