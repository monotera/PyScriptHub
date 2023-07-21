# BBC Articles Scraper

This script is designed to scrape articles from the BBC News website in the "Business" and "Technology" sections. It saves the scraped articles as JSON files and maintains an index of saved articles.

## Setup

To set up and run the script, follow these steps:

1. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain the following dependencies:
   ```
   requests
   beautifulsoup4
   ```

2. Copy the code into a Python file, e.g., `bbc_articles_scraper.py`.

3. Update the script's constants if needed:
   - `BASE_URLS`: Add or remove URLs as desired.
   - `SAVED_ARTICLES_DIR`: Choose the directory where the saved articles will be stored.
   - `SAVED_ARTICLES_INDEX`: Choose the file name of the JSON file that maintains the index of saved articles.
   - `SECTIONS_TO_EXCLUDE_BUISINESS_PAGE`: Add or remove section titles to exclude when scraping articles from the "Business" page.
   - `SECTIONS_TO_EXCLUDE_TECH_PAGE`: Add or remove section titles to exclude when scraping articles from the "Technology" page.

4. Run the script by executing the following command:
   ```
   python bbc_articles_scraper.py
   ```

   The script will create the necessary directories, load the saved articles index, and start scraping articles from the base URLs. The articles will be saved as JSON files in the specified directory.
