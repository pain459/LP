FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Install uvicorn
# RUN pip install uvicorn fastapi

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
