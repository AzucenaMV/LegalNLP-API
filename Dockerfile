FROM python:3.6.8

RUN pip install fastapi uvicorn lexnlp nltk

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
