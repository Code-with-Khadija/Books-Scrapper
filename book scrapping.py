from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("max")
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_page(driver):
    books = driver.find_elements(By.CLASS_NAME, "product_pod")
    results = []

    for book in books:
        try:

            title = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            rating = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()[-1]
            availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
            image_url = book.find_element(By.TAG_NAME, "img").get_attribute("src")

            results.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
                "image_url": image_url
            })
        except Exception as e:
            print(f"Error extracting book details: {e}")

    return results

# For multiple pages
def scrape_books(driver, num_pages):
    results = []
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"

    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}")
        driver.get(base_url.format(page))
        time.sleep(2)
        results.extend(scrape_page(driver))

    return results

# CSV file
def save_to_csv(results, filename="books.csv"):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "price", "rating", "availability", "image_url"])
            writer.writeheader()
            writer.writerows(results)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

def main():
    num_pages = int(input("Enter the number of pages to scrape: "))
    driver = init_driver()

    try:
        # book details
        results = scrape_books(driver, num_pages)

        print("\nBooks Found:")
        for idx, result in enumerate(results, 1):
            print(f"{idx}. Title: {result['title']}, Price: {result['price']}, Rating: {result['rating']}, Availability: {result['availability']}, Image URL: {result['image_url']}")

        save_to_csv(results)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()