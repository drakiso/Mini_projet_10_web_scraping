import csv
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

titles = soup.select('.product_pod h3 > a')
star_ratings = soup.find_all('p', class_='star-rating')
prices = soup.select('.price_color')

titles = [title.attrs['title'] for title in titles]
star_ratings = [star_rating.attrs['class'][1] for star_rating in star_ratings]
prices = [price.string for price in prices]

fieldnames = ['Title', 'Star_rating', 'Price']

with open('books_information.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, skipinitialspace=True)

    writer.writeheader()

    for title, star_rating, price in zip(titles, star_ratings, prices):
        writer.writerow({
            'Title': title,
            'Star_rating': star_rating,
            'Price': price
        })
