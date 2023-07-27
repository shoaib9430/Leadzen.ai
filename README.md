# Amazon Product Scraper
## Python 3.x

The Amazon Product Scraper is a Python script that allows you to scrape product information from Amazon's search results pages. It retrieves data such as product URLs, names, prices, ratings, and the number of reviews from multiple pages of Amazon search results. Additionally, it visits each product detail page to fetch further information like the product description, ASIN, manufacturer, and more.

## Features
Scrapes product information from multiple pages of Amazon search results.
Visits individual product detail pages to retrieve additional details.
Handles errors gracefully when certain product information is not available.

## Requirements
Python 3.x
requests library
BeautifulSoup library
csv module

### Installation
Clone the repository to your local machine:
https://github.com/shoaib9430/Leadzen.ai.git

### Navigate to the project directory:
cd amazon-product-scraper

### Install the required libraries:
pip install requests beautifulsoup4

### Run the scraper script:
python amazon_scraper.py

1. The script will start scraping the product data from Amazon. It will retrieve product URLs, names, prices, ratings, and the number of reviews from the search result pages. Then, it will visit each product detail page to fetch additional information, such as the product description, ASIN, and manufacturer.

2. The scraped data will be saved to a CSV file named "amazon_products.csv" in the same directory as the script.

## License
This project is licensed under the MIT License.

