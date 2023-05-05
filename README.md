# Web Scraping with Selenium, Docker, and Decision Lab

This project demonstrates how to perform web scraping using the Selenium WebDriver, run the scraping script in a Docker container, and use Decision Lab to dynamically configure scraping behavior.

## Overview

The project includes the following components:

- `Dockerfile`: Defines the Docker image that includes the necessary dependencies for running Selenium WebDriver and the Python scraping script.
- `requirements.txt`: Specifies the Python packages required for this project, including `selenium` and `decision_lab`.
- `scrape_with_decisionlab.py`: Contains a Selenium script that uses Decision Lab to configure scraping behavior based on a decision retrieved from Decision Lab.
- `Makefile`: Provides a set of commands to build and run the Docker container and execute the scraping scripts.

## Getting Started

### Prerequisites

- Docker: Ensure that Docker is installed on your machine.
- Decision Lab: Sign up for a Decision Lab account and obtain a UUID for accessing decisions.

### Setup

1. Clone this repository to your local machine.

2. Build the Docker image:
