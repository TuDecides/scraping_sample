# Web Scraping with Selenium, Docker, and Decision Lab

This project demonstrates how to perform web scraping using the Selenium WebDriver, run the scraping script in a Docker
container, and use Decision Lab to dynamically configure scraping behavior.

## Overview

The project includes the following components:

- `Dockerfile`: Defines the Docker image that includes the necessary dependencies for running Selenium WebDriver and the
  Python scraping script.
- `requirements.txt`: Specifies the Python packages required for this project, including `selenium` and `decision_lab`.
- `scrape_with_decisionlab.py`: Contains a Selenium script that uses Decision Lab to configure scraping behavior based
  on a decision retrieved from Decision Lab.
- `Makefile`: Provides a set of commands to build and run the Docker container and execute the scraping scripts.

## Getting Started

### Prerequisites

- Docker: Ensure that Docker is installed on your machine.
- Decision Lab: Sign up for a Decision Lab account and obtain a UUID for accessing decisions.

### Setup

1. Clone this repository to your local machine.

2. Build the Docker image:
   `make build`

3. Run the Docker container:
   `make run_decisionlab`

4. In decisionlab, you can use this configuration

``` 
{ "name": "scraping_configuration", 
  "data": { 
           "url": "http://quotes.toscrape.com/", 
           "elements": { "quotes": true, 
                        "authors": true 
                        }, 
           "pages_to_scrape": 1 
           }
         }
```

Some more possible configurations: 

``` 
{
  "name": "scraping_configuration",
  "data": {
    "url": "http://quotes.toscrape.com/",
    "elements": {
      "quotes": true,
      "authors": true
    },
    "pages_to_scrape": 2
  }
}

```

Only scraping quotes
``` 
{
  "name": "scraping_configuration",
  "data": {
    "url": "http://quotes.toscrape.com/",
    "elements": {
      "quotes": true,
      "authors": false
    },
    "pages_to_scrape": 1
  }
}


```

Only getting quotes authors: 
```  
{
  "name": "scraping_configuration",
  "data": {
    "url": "http://quotes.toscrape.com/",
    "elements": {
      "quotes": false,
      "authors": true
    },
    "pages_to_scrape": 1
  }
}


```