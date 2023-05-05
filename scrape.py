import requests
from bs4 import BeautifulSoup


def scrape_quotes(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with the class 'quote'
        quotes_elements = soup.find_all(class_='quote')

        # Extract the quotes and authors from the elements
        quotes = []
        for quote_element in quotes_elements:
            quote_text = quote_element.find(class_='text').text
            quote_author = quote_element.find(class_='author').text
            quotes.append({
                'quote': quote_text,
                'author': quote_author
            })
        return quotes
    else:
        print(f"Failed to retrieve the quotes. Status code: {response.status_code}")
        return []


# URL of the Quotes to Scrape website
url = 'http://quotes.toscrape.com/'

# Scrape the quotes from the website
quotes = scrape_quotes(url)
for quote in quotes:
    print('\n\n\n\n.......\n\n\n\n')
    print(f'"{quote["quote"]}" - {quote["author"]}')
