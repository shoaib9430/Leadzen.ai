import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape product details from the product listing page
def scrape_product_listing(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    for product in soup.select("div.s-result-item"):
        try:
            product_url = product.select_one("a.a-link-normal.s-no-outline")["href"]
            product_name = product.select_one("span.a-text-normal").text.strip()
            product_price = product.select_one("span.a-price span.a-offscreen").text.strip()
            rating_element = product.select_one("span.a-icon-alt")
            rating = rating_element.text.strip().split()[0] if rating_element else "N/A"
            num_reviews_element = product.select_one("span.a-size-base")
            num_reviews = num_reviews_element.text.strip().split()[0] if num_reviews_element else "N/A"

            products.append({
                "Product URL": "https://www.amazon.in" + product_url,
                "Product Name": product_name,
                "Product Price": product_price,
                "Rating": rating,
                "Number of Reviews": num_reviews
            })
        except Exception as e:
            print("Error parsing product:", e)
            continue

    return products

# Function to scrape additional product details from the product detail page
def scrape_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        description = soup.select_one("meta[name='description']")
        description = description["content"] if description else "N/A"

        asin_element = soup.select_one("th:contains('ASIN') + td")
        asin = asin_element.text.strip() if asin_element else "N/A"

        product_description_element = soup.select_one("h1 span.a-text-normal")
        product_description = product_description_element.text.strip() if product_description_element else "N/A"

        manufacturer_element = soup.select_one("th:contains('Manufacturer') + td")
        manufacturer = manufacturer_element.text.strip() if manufacturer_element else "N/A"

        return {
            "Description": description,
            "ASIN": asin,
            "Product Description": product_description,
            "Manufacturer": manufacturer
        }
    except Exception as e:
        print("Error parsing product details:", e)
        return None

# Main function to execute the scraping
def main():
    base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1{}"
    num_pages = 20
    products_data = []

    for page_number in range(1, num_pages + 1):
        url = base_url.format(page_number)
        print("Scraping page", page_number)
        products_data += scrape_product_listing(url)

    with open("amazon_products.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews", "Description", "ASIN", "Product Description", "Manufacturer"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products_data:
            product_details = scrape_product_details(product["Product URL"])
            if product_details:
                product.update(product_details)
                writer.writerow(product)

if __name__ == "__main__":
    main()
