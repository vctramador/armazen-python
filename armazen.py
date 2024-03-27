import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraindo informações de livros
Livros = []
for book in soup.find_all('article', class_='product_pod'):
        titulo = book.h3.a.attrs['title']
        preco = book.find('p', class_='price_color').text
        estoque = book.find('p', class_='instock availability').text.strip()

        Livros.append({'Titulo': titulo, 'Preço': preco, 'Estoque': estoque})

with open('livros.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Titulo', 'Preço', 'Estoque'])
    writer.writeheader()
    for Livro in Livros:
        writer.writerow(Livro)

print('Dados extraidos e armazenados em Livros.csv')