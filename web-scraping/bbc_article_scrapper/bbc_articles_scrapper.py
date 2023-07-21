import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URLS = ['https://www.bbc.com/news/business',
             'https://www.bbc.com/news/technology']
SAVED_ARTICLES_DIR = 'saved_articles'
SAVED_ARTICLES_INDEX = 'saved_articles_index.json'
SECTIONS_TO_EXCLUDE_BUISINESS_PAGE = ['nw-c-Features&Analysis__title', 'nw-c-Watch/Listen__title',
                                      'nw-c-SpecialReports__title']
SECTIONS_TO_EXCLUDE_TECH_PAGE = ["nw-c-Watch/Listen__title", "nw-c-Features&Analysis__title"]


def save_article(url, title, body):
    file_name = url.replace('/', '_') + '.json'
    file_path = os.path.join(SAVED_ARTICLES_DIR, file_name)
    with open(file_path, 'w') as f:
        json.dump({'title': title, 'body': body}, f)


def load_saved_articles_index():
    if not os.path.exists(SAVED_ARTICLES_INDEX):
        return {}
    with open(SAVED_ARTICLES_INDEX, 'r') as f:
        return json.load(f)


def save_saved_articles_index(index):
    with open(SAVED_ARTICLES_INDEX, 'w') as f:
        json.dump(index, f)


def is_article_saved(url, saved_articles_index):
    return url in saved_articles_index


def mark_article_as_saved(url, saved_articles_index):
    saved_articles_index[url] = True
    save_saved_articles_index(saved_articles_index)


def scrape_articles(url, saved_articles_index):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    excluded_sections = SECTIONS_TO_EXCLUDE_BUISINESS_PAGE if url == 'https://www.bbc.com/news/business' else SECTIONS_TO_EXCLUDE_TECH_PAGE
    excluded_divs = soup.find_all('div', attrs={'aria-labelledby': excluded_sections})

    for link in soup.find_all('a'):
        parent_div = link.find_parent('div', attrs={'aria-labelledby': excluded_sections})
        if parent_div in excluded_divs:
            continue

        article_url = urljoin(url, link.get('href'))
        if not article_url.startswith(url) or is_article_saved(article_url, saved_articles_index):
            continue

        response = requests.get(article_url)
        article_soup = BeautifulSoup(response.text, 'html.parser')

        title = article_soup.find('h1').text
        body = ' '.join([p.text for p in article_soup.find_all('p')])

        save_article(article_url, title, body)
        mark_article_as_saved(article_url, saved_articles_index)


def main():
    if not os.path.exists(SAVED_ARTICLES_DIR):
        os.makedirs(SAVED_ARTICLES_DIR)

    saved_articles_index = load_saved_articles_index()

    for url in BASE_URLS:
        scrape_articles(url, saved_articles_index)


if __name__ == '__main__':
    main()
