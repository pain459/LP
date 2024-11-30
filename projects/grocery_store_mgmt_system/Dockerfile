FROM python:3.10-slim

WORKDIR /sku_db

COPY ./sku_db /sku_db

RUN pip install --no-cache-dir fastapi uvicorn
# no need to install sqlite3 seperately.

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
