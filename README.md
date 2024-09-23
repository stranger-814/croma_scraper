# Croma TV Scraper and Search Engine

This project involves two main components:
1. **Data Collection (Scraping)**: Using Scrapy to collect data from the Croma website for the products in the 'Televisions & Accessories > LED TVs > 4K Ultra HD TVs' category.
2. **Search Engine**: Building a search engine to filter and display relevant products based on user input.

## Project Structure
- `croma_spider.py`: Scrapy spider to scrape product details from the Croma website.
- `tv_search_engine.py`: Python script that implements a TV search engine using the data collected from the scraping process.

## Prerequisites
- Python 3.x
- Scrapy library
- CSV library (standard in Python)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/stranger-814/croma_scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd croma_scraper
    ```
3. Install the required dependencies:
    ```bash
    pip install scrapy
    ```

## Part 1: Data Collection with Scrapy

The `croma_spider.py` script scrapes product details from the Croma website, such as listing position, title, brand, MRP, price, count of ratings, count of reviews, average rating score, product URL, and image URL. This data is stored in a CSV file.

### How to Run
1. Execute the following command to start scraping and save the output to `cromaTV.csv`:
    ```bash
    scrapy crawl croma_api_spider -o cromaTV.csv -t csv
    ```
2. The data will be stored in a file named `cromaTV.csv` in the project directory.

   ![csv](https://github.com/user-attachments/assets/eebc1bc6-7f23-412f-9a28-15f61eaf6032)

## Part 2: Building the TV Search Engine

The `tv_search_engine.py` script reads the `cromaTV.csv` file and provides a search engine to filter TV products based on user input.

### How to Run
1. Ensure the `cromaTV.csv` file is in the project directory.
2. Run the search engine script:
    ```bash
    python tv_search_engine.py
    ```
3. The program will prompt you to enter search criteria for the TV you are looking for, e.g., `Samsung 4K 43 inch TV`.
4. To exit, type `STOP`.

### Output
The search engine provides:
- Top 3 best listing position products matching your criteria
- Top 3 lowest price products
- Top 3 highest average rating products

## Example Usage
![Screenshot 2024-09-23 120148](https://github.com/user-attachments/assets/8a46e609-230f-41af-9a2d-5475db5bb8a7)
![Screenshot 2024-09-23 120225](https://github.com/user-attachments/assets/df565924-b5ad-4d19-8d4c-6baf466b0095)




## Important Notes
- Ensure your internet connection is stable for data scraping.
- The `tv_search_engine.py` script is case-insensitive, so you can enter search criteria in any case.

## Author
- **Sandesh Lingayat** 

