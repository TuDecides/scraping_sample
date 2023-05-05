import json
from decisionlab import DecisionLab
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By


class Configuration:
    def __init__(self, decision):
        decision_data = json.loads(decision)
        self.data = decision_data["data"]  # Here's the change

        # Validate the configuration
        self.validate()

    def validate(self):
        # You can add more checks to validate the configuration
        assert "url" in self.data
        assert "elements" in self.data
        assert "quotes" in self.data["elements"]
        assert "authors" in self.data["elements"]
        assert "pages_to_scrape" in self.data

    @property
    def url(self):
        return self.data["url"]

    @property
    def scrape_quotes(self):
        return self.data["elements"]["quotes"]

    @property
    def scrape_authors(self):
        return self.data["elements"]["authors"]

    @property
    def pages_to_scrape(self):
        return self.data["pages_to_scrape"]


def scrape_quotes(decision_lab):
    # Get the scraping configuration decision
    decision = decision_lab.get_decision('scraping_configuration')
    config = Configuration(decision)
    print(f"\n\n\nScraping configuration: {config.data}\n\n\n")

    # Extract configuration values from the decision
    url = config.url
    scrape_quotes = config.scrape_quotes
    scrape_authors = config.scrape_authors
    pages_to_scrape = config.pages_to_scrape

    # Configure Chrome WebDriver options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
    chrome_options.add_argument("--headless")

    # Initialize the WebDriver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(10)
    # Navigate to the URL specified in the decision
    driver.get(url)

    # Scrape the desired elements based on the decision
    quotes = []
    for page in range(pages_to_scrape):
        quote_elements = driver.find_elements(By.CLASS_NAME, 'quote')
        for quote_element in quote_elements:
            quote_text = quote_element.find_element(By.CLASS_NAME, 'text').text
            if scrape_authors:
                quote_author = quote_element.find_element(By.CLASS_NAME, 'author').text
            else:
                quote_author = None
            if scrape_quotes:
                quotes.append({
                    'quote': quote_text,
                    'author': quote_author
                })
            else:
                quotes.append({
                    'author': quote_author
                })

        # Go to the next page if applicable
        if page < pages_to_scrape - 1:
            next_button = driver.find_element(By.CSS_SELECTOR, '.next a')
            next_button.click()
            time.sleep(2)

    # Close the browser window
    driver.quit()

    return quotes


# Create an instance of DecisionLab with UUID
dl = DecisionLab(uuid='4c8fc261-92de-4dea-8ed8-9418a577d503')

# Scrape the quotes based on the decision
quotes = scrape_quotes(dl)
for quote in quotes:
    print(f'"{quote.get("quote", "")}" - {quote.get("author")}')
