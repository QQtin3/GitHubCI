FROM python:3.9
WORKDIR /api

COPY ./ /api

RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "python createCollection.py && fastapi run main.py"]
