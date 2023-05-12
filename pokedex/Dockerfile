FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./app/* ./
COPY ./app/templates/* ./templates/

EXPOSE 8080

CMD ["python", "pokedex.py"]
