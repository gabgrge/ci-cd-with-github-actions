# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install pytest for unit tests
RUN pip install pytest

# Install selenium for integration tests
RUN pip install selenium

# Install Chrome WebDriver
RUN apt-get update && apt-get install -y \
    chromium-driver

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]