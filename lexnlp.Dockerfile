FROM python:3.6.8

ENV SPACY_MODEL=en_core_web_sm
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/AzucenaMV/LegalNLP-API.git ~/legalnlp
WORKDIR root/legalnlp/app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader popular

EXPOSE 5001

CMD ["python", "main.py"]
