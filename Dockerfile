# Dockerfile
FROM python:3.10-slim-buster

WORKDIR /app

# Install Chrome WebDriver
RUN apt-get update && apt-get install -y \
    curl unzip xvfb libxi6 libgconf-2-4 \
    && curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb \
    && dpkg -i /chrome.deb || apt-get install -yf \
    && rm /chrome.deb \
    && curl https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -o /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]