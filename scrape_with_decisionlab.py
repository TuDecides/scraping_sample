import json
from decisionlab import DecisionLab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def scrape_quotes(decision_lab):
    # Get the scraping configuration decision
    decision = json.loads(decision_lab.get_decision('scraping_configuration'))

    # Extract configuration values from the decision
    url = decision['data']['url']
    scrape_quotes = decision['data']['elements']['quotes']
    scrape_authors = decision['data']['elements']['authors']
    pages_to_scrape = decision['data']['pages_to_scrape']

    # Configure Chrome WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
    chrome_options.headless = True  # Run in headless mode

    # Initialize the WebDriver
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)

    # Navigate to the URL specified in the decision
    driver.get(url)

    # Scrape the desired elements based on the decision
    quotes = []
    for page in range(pages_to_scrape):
        if scrape_quotes:
            quote_elements = driver.find_elements_by_class_name('quote')
            for quote_element in quote_elements:
                quote_text = quote_element.find_element_by_class_name('text').text
                if scrape_authors:
                    quote_author = quote_element.find_element_by_class_name('author').text
                else:
                    quote_author = None
                quotes.append({
                    'quote': quote_text,
                    'author': quote_author
                })

        # Go to the next page if applicable
        if page < pages_to_scrape - 1:
            next_button = driver.find_element_by_css_selector('.next a')
            next_button.click()
            time.sleep(2)

    # Close the browser window
    driver.quit()

    return quotes

# Create an instance of DecisionLab with UUID
decision_lab = DecisionLab(uuid='4c8fc261-92de-4dea-8ed8-9418a577d503')

# Scrape the quotes based on the decision
quotes = scrape_quotes(decision_lab)
for quote in quotes:
    print(f'"{quote["quote"]}" - {quote["author"]}')
