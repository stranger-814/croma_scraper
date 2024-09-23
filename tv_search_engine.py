import csv

class TVSearchEngine:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)

    def load_products(self, csv_file):
        products = []
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products

    def search(self, query):
        #Filter products matching the query
        query_lower = query.lower()
        filtered_products = [
            product for product in self.products if query_lower in product['Title'].lower()
        ]

        if not filtered_products:
            return [], [], []

        #Top 3 best/top listing position products
        top_listing = sorted(filtered_products, key=lambda x: int(x['Listing Position']))[:3]

        #Top 3 lowest price products
        lowest_price = sorted(filtered_products, key=lambda x: float(x['Price'] or 0))[:3]

        #Top 3 highest average rating products
        highest_rating = sorted(filtered_products, key=lambda x: float(x['Average Rating Score'] or 0), reverse=True)[:3]

        return top_listing, lowest_price, highest_rating

def main():
    csv_file = 'cromaTV.csv'  #Path to the CSV file
    engine = TVSearchEngine(csv_file)

    while True:
        user_input = input("Enter your search criteria (or type 'STOP' to exit): ").strip()
        if user_input.upper() == 'STOP':
            break
        
        top_listing, lowest_price, highest_rating = engine.search(user_input)

        if not top_listing and not lowest_price and not highest_rating:
            print("\nNo products found matching your search criteria. Please try again with a different query.\n")
            continue

        print("\nTop 3 Best Listing Position Products:")
        if top_listing:
            for product in top_listing:
                print(f"- {product['Title']} | Price: {product['Price']} | Brand: {product['Brand']} | URL: {product['Product URL']}")
        else:
            print("No products found in the best listing position category.")

        print("\nTop 3 Lowest Price Products:")
        if lowest_price:
            for product in lowest_price:
                print(f"- {product['Title']} | Price: {product['Price']} | Brand: {product['Brand']} | URL: {product['Product URL']}")
        else:
            print("No products found in the lowest price category.")

        print("\nTop 3 Highest Average Rating Products:")
        if highest_rating:
            for product in highest_rating:
                print(f"- {product['Title']} | Average Rating: {product['Average Rating Score']} | Brand: {product['Brand']} | URL: {product['Product URL']}")
        else:
            print("No products found in the highest average rating category.")

if __name__ == '__main__':
    main()
