FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK WordNet corpus
RUN python -m nltk.downloader wordnet

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
