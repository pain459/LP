FROM python:3.8
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
# Copy the voter database into the image
COPY voters.db /app/voters.db
CMD ["python", "app.py"]
