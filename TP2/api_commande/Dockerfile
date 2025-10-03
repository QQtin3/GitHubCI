FROM python:3.9
WORKDIR /api_commande

COPY ./ /api_commande

RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "fastapi run main.py"]