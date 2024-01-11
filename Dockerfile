# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install Chrome WebDriver
RUN apt-get update && apt-get install -y \
    chromium-driver

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]