FROM python:3.6.8

ENV SPACY_MODEL=en_core_web_sm
RUN pip install https://blackstone-model.s3-eu-west-1.amazonaws.com/en_blackstone_proto-0.0.1.tar.gz
RUN python -m nltk.downloader all
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./app /app
EXPOSE 5001

CMD ["python", "/app/main.py"]
