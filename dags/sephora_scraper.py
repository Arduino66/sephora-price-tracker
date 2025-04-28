from playwright.sync_api import sync_playwright
import csv
import time

# List of category URLs to scrape
categories = [
    "https://www.sephora.fr/shop/soin-visage/besoins/soin-anti-imperfections-c441/",
    #"https://www.sephora.fr/shop/soin-visage/besoins/soin-anti-rides-et-anti-age-c7636/",
   # "https://www.sephora.fr/shop/soin-visage/besoins/soin-hydratant-et-nourrissant-c7634/"
]

def scrape_sephora():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for category_url in categories:
            print(f"\nScraping category: {category_url}")

            # CSV filename based on category
            raw_category = category_url.rstrip('/').split("/")[-1]
            clean_category = raw_category.rsplit("-", 1)[0].replace("-", " ").capitalize()

            filename = f"raw_products_{clean_category}.csv"

            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Brand", "Product Name", "Price", "Rating", "Reviews", "Ingredients", "Category"])

                try:
                    page.goto(category_url)
                except Exception as e:
                    print(f"❌ Error loading category page {category_url}: {e}")
                    continue

                # Close cookie popup if found
                try:
                    page.wait_for_selector('button:has-text("Continuer sans accepter")', timeout=500)
                    page.click('button:has-text("Continuer sans accepter")')
                    print("✅ Cookie popup closed!")
                except:
                    print("✅ No cookie popup found.")

                # Load more products
                try:
                    page.wait_for_selector('button:has-text("Voir plus de produits")', timeout=500)
                    page.click('button:has-text("Voir plus de produits")')
                    print("More products loaded!")
                except:
                    print("Button not found!")

                # Wait for product list
                page.wait_for_selector('ul#search-result-items')

                # Scroll to the bottom to load all products
                '''previous_height = 0
                while True:
                    current_height = page.evaluate("document.body.scrollHeight")
                    if current_height == previous_height:
                        break  # Stop if no new content is loaded
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    page.wait_for_timeout(5000)  # Wait a bit for new products to load
                    previous_height = current_height

                print("Scrolled to the bottom!")'''


                # Collect all product links
                product_cards = page.query_selector_all('ul#search-result-items li[data-product-index]')
                product_links = []

                for card in product_cards:
                    link = card.query_selector('a').get_attribute('href')
                    if link:
                        if link.startswith("/"):
                            full_url = "https://www.sephora.fr" + link
                        else:
                            full_url = link
                        product_links.append(full_url)

                print(f"🔎 Found {len(product_links)} products.")

                # Loop through product links
                for i, product_url in enumerate(product_links, start=1):
                    try:
                        page.goto(product_url)
                        page.wait_for_selector('div.product-detail', timeout=5000)

                        # Product Name
                        name_el = page.query_selector('.product-name')
                        product_name = name_el.inner_text().strip() if name_el else "N/A"

                        # Brand
                        brand_el = page.query_selector('.brand-name')
                        brand = brand_el.inner_text().strip() if brand_el else "N/A"

                        # Price
                        price_el = page.query_selector('.product-price')
                        price = price_el.inner_text().strip() if price_el else "N/A"

                        # Rating
                        rating_el = page.query_selector('.bv-overall-score')
                        if rating_el:
                            rating_html = rating_el.inner_html()
                            rating = rating_html.split('<br>')[0].strip()
                        else:
                            rating = "N/A"


                        # Number of reviews
                        reviews_el = page.query_selector('.bv-number-review')
                        reviews = reviews_el.inner_text().strip() if reviews_el else "N/A"

                        # Open Ingredients tab
                        try:
                            page.wait_for_selector('span:has-text("Ingrédients")', timeout=500)
                            page.click('span:has-text("Ingrédients")')
                            page.wait_for_timeout(1000)
                        except:
                            print("Ingrédients tab not found")

                        # Extract ingredients
                        ingredients_el = page.query_selector('.ingredients-content')
                        if ingredients_el:
                            ingredients_text = ingredients_el.inner_text().strip().lower()
                            ingredients = ingredients_text.split("cette")[0].strip()
                        else:
                            ingredients = "N/A"


                        # Write to CSV
                        writer.writerow([brand, product_name, price, rating, reviews, ingredients, clean_category])

                        print(f"✅ Scraped {i}/{len(product_links)}: {product_name}")

                        # Sleep a tiny bit to be nice to the server
                        time.sleep(0.5)

                    except Exception as e:
                        print(f"❌ Error scraping product {product_url}: {e}")
                        continue

            print(f"📁 Finished scraping {clean_category}. Data saved to {filename}")

        browser.close()

scrape_sephora()
