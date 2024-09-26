import scrapy
import json

class CromaApiSpider(scrapy.Spider):
    name = "croma_api_spider"
    allowed_domains = ["api.croma.com"]
    start_urls = [
        "https://api.croma.com/searchservices/v1/category/999?currentPage=0&query=:relevance&fields=FULL&channel=WEB&channelCode=400049"
    ]

    def __init__(self):
        self.listing_position = 1

    def parse(self, response):
        #Load the JSON response
        data = json.loads(response.text)

        #Extracting product data
        products = data.get('products', [])

        for product in products:
            url_parts = product.get('url', '').split('-')
            brand = url_parts[0].strip('/') if len(url_parts) > 1 else None
            brand = brand.capitalize() if brand else brand

            #Forming the complete Product URL
            product_url = product.get('url')
            full_product_url = f"https://www.croma.com{product_url}" if product_url else None

            yield {
                'Listing Position': self.listing_position,
                'Title': product.get('name'),
                'Brand': brand,
                'MRP': product.get('mrp', {}).get('value'),
                'Price': product.get('price', {}).get('value'),
                'Average Rating Score': product.get('averageRating'),  
                'Count of Ratings': product.get('numberOfRatings'),    
                'Count of Reviews': product.get('numberOfReviews'), 
                'Product URL': full_product_url,
                'Image_url' : product.get("plpImage")  
            }
            self.listing_position += 1

        #pagination
        current_page = data.get('pagination', {}).get('currentPage')
        total_pages = data.get('pagination', {}).get('totalPages')

        if current_page is not None and total_pages is not None and current_page < total_pages - 1:
            next_page = current_page + 1
            next_page_url = f"https://api.croma.com/searchservices/v1/category/999?currentPage={next_page}&query=:relevance&fields=FULL&channel=WEB&channelCode=400049"
            yield scrapy.Request(url=next_page_url, callback=self.parse)
