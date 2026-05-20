# DAY 19 EXERCISES - 20th May 2026
# Topic: Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

# Exercise 1: Basic scraping
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,
                     "html.parser")

print(f"Status: {response.status_code}")
print(f"Page title: {soup.title.text}")
print(f"First h1: {soup.find('h1').text}")

# Exercise 2: Find all books
books = soup.find_all("article",
                       class_="product_pod")
print(f"\nTotal books found: {len(books)}")

print("\nFirst 5 books:")
for book in books[:5]:
    title = book.find("h3").find("a")["title"]
    price = book.find("p",
                      class_="price_color").text
    rating = book.find("p",
                       class_="star-rating")
    rating_class = rating["class"][1]
    print(f"  Title : {title[:40]}")
    print(f"  Price : {price}")
    print(f"  Rating: {rating_class}")
    print("  " + "-" * 35)

# Exercise 3: Scrape quotes
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,
                     "html.parser")

quotes = soup.find_all("div",
                        class_="quote")
print(f"\nTotal quotes: {len(quotes)}")

for quote in quotes[:3]:
    text = quote.find("span",
                      class_="text").text
    author = quote.find("small",
                        class_="author").text
    tags = quote.find_all("a",
                          class_="tag")
    tag_list = [tag.text for tag in tags]
    print(f"\nQuote : {text[:60]}...")
    print(f"Author: {author}")
    print(f"Tags  : {tag_list}")

# Exercise 4: Scrape multiple pages
url = "https://quotes.toscrape.com"
all_quotes = []
page = 1

while page <= 3:
    response = requests.get(
        f"{url}/page/{page}/")
    soup = BeautifulSoup(response.text,
                         "html.parser")
    quotes = soup.find_all("div",
                            class_="quote")
    for quote in quotes:
        text = quote.find(
            "span", class_="text").text
        author = quote.find(
            "small", class_="author").text
        all_quotes.append({
            "text": text,
            "author": author,
            "page": page
        })
    print(f"Page {page}: "
          f"{len(quotes)} quotes scraped")
    page += 1

print(f"\nTotal quotes scraped: "
      f"{len(all_quotes)}")

# Exercise 5: Save scraped data
import json

with open("scraped_quotes.json",
          "w") as file:
    json.dump(all_quotes, file, indent=4)
print("Quotes saved to scraped_quotes.json!")

with open("scraped_quotes.json",
          "r") as file:
    loaded = json.load(file)
print(f"Loaded {len(loaded)} quotes!")
print(f"First quote: "
      f"{loaded[0]['text'][:50]}...")
