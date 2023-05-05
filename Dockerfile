# Use the multi-architecture variant of the selenium/standalone-chrome image
FROM seleniarm/standalone-chromium:latest

WORKDIR /usr/src/app

COPY requirements.txt .

# Install Python3, pip3, and venv
RUN sudo apt-get update && \
    sudo apt-get install -y python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv venv

RUN . venv/bin/activate && pip install --upgrade pip setuptools selenium urllib3 &&  \
    pip install -r requirements.txt \
    && pip install --upgrade selenium urllib3 \
    && pip install ipdb


COPY . .

ENTRYPOINT ["venv/bin/python3", "scrape.py"]