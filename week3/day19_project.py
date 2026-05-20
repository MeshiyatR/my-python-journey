# DAY 19 PROJECT - Smart Book Scraper
# 20th May 2026

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime

BASE_URL = "https://books.toscrape.com"

RATING_MAP = {
    "One": 1, "Two": 2,
    "Three": 3, "Four": 4, "Five": 5
}

def scrape_page(url):
    try:
        response = requests.get(
            url, timeout=10)
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(
            response.text, "html.parser")
        books = soup.find_all(
            "article",
            class_="product_pod")
        page_books = []
        for book in books:
            title = book.find(
                "h3").find("a")["title"]
            price = book.find(
                "p",
                class_="price_color"
            ).text.replace("Â", "").strip()
            rating_class = book.find(
                "p",
                class_="star-rating"
            )["class"][1]
            rating = RATING_MAP.get(
                rating_class, 0)
            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()
            page_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })
        return page_books
    except Exception as e:
        print(f"Error scraping: {e}")
        return []

def scrape_books(num_pages=3):
    print(f"\nScraping {num_pages} pages...")
    all_books = []
    for page in range(1, num_pages + 1):
        if page == 1:
            url = f"{BASE_URL}/index.html"
        else:
            url = (f"{BASE_URL}/catalogue/"
                   f"page-{page}.html")
        books = scrape_page(url)
        all_books.extend(books)
        print(f"  Page {page}: "
              f"{len(books)} books found")
    print(f"\nTotal books scraped: "
          f"{len(all_books)}")
    return all_books

def analyze_books(books):
    if not books:
        print("No books to analyze!")
        return None
    df = pd.DataFrame(books)
    df["price_num"] = df["price"].str.extract(
        r"(\d+\.\d+)").astype(float)
    return df

def show_all_books(df):
    print("\n" + "=" * 60)
    print("           ALL BOOKS")
    print("=" * 60)
    for _, book in df.head(10).iterrows():
        stars = "⭐" * book["rating"]
        print(f"  {book['title'][:40]}")
        print(f"  Price: {book['price']}"
              f"  {stars}")
        print("  " + "-" * 45)
    print(f"\n  Showing 10 of "
          f"{len(df)} books")

def show_statistics(df):
    print("\n" + "=" * 45)
    print("        BOOK STATISTICS")
    print("=" * 45)
    print(f"  Total books  : {len(df)}")
    print(f"  Avg price    : "
          f"£{df['price_num'].mean():.2f}")
    print(f"  Cheapest     : "
          f"£{df['price_num'].min():.2f}")
    print(f"  Most expensive: "
          f"£{df['price_num'].max():.2f}")
    print(f"  Avg rating   : "
          f"{df['rating'].mean():.1f}/5")

    print("\n  Books by rating:")
    rating_counts = df["rating"].value_counts(
    ).sort_index(ascending=False)
    for rating, count in rating_counts.items():
        stars = "⭐" * rating
        print(f"  {stars}: {count} books")
    print("=" * 45)

def top_rated_books(df):
    print("\n" + "=" * 50)
    print("         TOP RATED BOOKS")
    print("=" * 50)
    top = df[df["rating"] == 5].head(5)
    if top.empty:
        print("  No 5-star books found!")
    else:
        for _, book in top.iterrows():
            print(f"  ⭐⭐⭐⭐⭐ "
                  f"{book['title'][:40]}")
            print(f"  Price: {book['price']}")
            print()
    print("=" * 50)

def cheapest_books(df):
    print("\n" + "=" * 50)
    print("         CHEAPEST BOOKS")
    print("=" * 50)
    cheap = df.nsmallest(5, "price_num")
    for _, book in cheap.iterrows():
        stars = "⭐" * book["rating"]
        print(f"  {book['price']} — "
              f"{book['title'][:35]}")
        print(f"  Rating: {stars}")
        print()
    print("=" * 50)

def search_books(df):
    keyword = input(
        "\nEnter search keyword: ").lower()
    results = df[df["title"].str.lower(
    ).str.contains(keyword)]
    print(f"\nFound {len(results)} books "
          f"matching '{keyword}':")
    if results.empty:
        print("  No books found!")
    else:
        for _, book in results.iterrows():
            stars = "⭐" * book["rating"]
            print(f"  {book['title'][:40]}")
            print(f"  {book['price']} {stars}")
            print()

def save_to_files(df):
    timestamp = datetime.now().strftime(
        "%d%m%Y_%H%M")
    json_file = f"books_{timestamp}.json"
    csv_file = f"books_{timestamp}.csv"

    df.to_json(json_file,
               orient="records",
               indent=4)
    df.to_csv(csv_file, index=False)

    print(f"\nSaved to:")
    print(f"  JSON: {json_file}")
    print(f"  CSV : {csv_file}")

# Main program
print("=" * 50)
print("       SMART BOOK SCRAPER")
print("   Real data from the internet!")
print("=" * 50)

print("\nInitializing — scraping data...")
books_data = scrape_books(num_pages=3)
df = analyze_books(books_data)

if df is not None:
    while True:
        print("\n1 - View all books")
        print("2 - Book statistics")
        print("3 - Top rated books")
        print("4 - Cheapest books")
        print("5 - Search books")
        print("6 - Save to JSON and CSV")
        print("7 - Scrape more pages")
        print("8 - Quit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            show_all_books(df)
        elif choice == "2":
            show_statistics(df)
        elif choice == "3":
            top_rated_books(df)
        elif choice == "4":
            cheapest_books(df)
        elif choice == "5":
            search_books(df)
        elif choice == "6":
            save_to_files(df)
        elif choice == "7":
            pages = int(input(
                "How many pages: "))
            books_data = scrape_books(pages)
            df = analyze_books(books_data)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
