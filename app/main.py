import uvicorn
import regex
import nltk
import types
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from collections import OrderedDict
from models.Leg import Leg
from models.NamedEntity import NamedEntity
from models.Abrv import Abrv
import lexnlp.extract.en.definitions
import lexnlp.extract.en.durations
import lexnlp.extract.en.regulations
import lexnlp.extract.en.conditions
import lexnlp.extract.en.constraints
from lexnlp.extract.en.entities.nltk_maxent import get_company_annotations
import lexnlp.extract.en.acts
import lexnlp.extract.en.dates
import lexnlp.extract.en.trademarks
import lexnlp.extract.en.percents
import lexnlp.extract.en.money
import lexnlp.extract.en.amounts
import lexnlp.extract.en.entities.nltk_maxent
import lexnlp.extract.en.entities.nltk_re
from blackstone.pipeline.abbreviations import AbbreviationDetector
from blackstone.utils.legislation_linker import extract_legislation_relations
from blackstone.rules import CITATION_PATTERNS

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class Request(BaseModel):
    text: str

#nlp = spacy.load("en_blackstone_proto")
#abbreviation_pipe = AbbreviationDetector(nlp)
#nlp.add_pipe(abbreviation_pipe)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Working"}

@app.post("/act")
def Act(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.acts.get_act_list(item.text)))


@app.post("/amount")
def Amount(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.amounts.get_amounts(item.text))))


@app.post("/constraint")
def Constraint(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.extract.en.constraints.get_constraints(item.text)))


@app.post("/company")
def Company(item: Request):
    return JSONResponse(content=jsonable_encoder(
        (list(get_company_annotations(item.text)))))


@app.post("/date")
def Date(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.dates.get_dates(item.text))))


@app.post("/definition")
def Definition(item: Request):
    return JSONResponse(
        content=jsonable_encoder(list(lexnlp.extract.en.definitions.get_definitions(item.text, True, True))))


@app.post("/duration")
def Duration(item: Request):
    print(item.text)
    print(lexnlp.extract.en.durations.get_durations(item.text))
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.durations.get_durations(item.text, return_sources = True))))

@app.post("/money")
def Money(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.money.get_money(item.text, True, 4))))


@app.post("/regulation")
def Regulation(item: Request):
    return JSONResponse(
        content=jsonable_encoder(list(lexnlp.extract.en.regulations.get_regulations(item.text, True, True))))

@app.post("/sentences")
def Sentences(item: Request):
    return JSONResponse(content=jsonable_encoder(lexnlp.nlp.en.segments.sentences.get_sentence_list(item.text)))


@app.post("/trademark")
def Regulation(item: Request):
    return JSONResponse(content=jsonable_encoder(list(lexnlp.extract.en.trademarks.get_trademarks(item.text))))

def findall(text, sub):
    """Return all indices at which substring occurs in text"""
    return [
        index
        for index in range(len(text) - len(sub) + 1)
        if text[index:].startswith(sub)
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)