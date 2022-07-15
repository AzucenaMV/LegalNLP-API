FROM python:3.6.8

ENV SPACY_MODEL=en_core_web_sm
RUN python -m pip install --upgrade pip
#RUN pip install https://blackstone-model.s3-eu-west-1.amazonaws.com/en_blackstone_proto-0.0.1.tar.gz
RUN git clone https://github.com/AzucenaMV/LegalNLP-API.git ~/legalnlp
WORKDIR root/legalnlp/app
RUN pip install -r requirements.txt
#RUN python -m nltk.downloader all
RUN python -m nltk.downloader punkt

EXPOSE 5001

CMD ["python", "main.py"]
