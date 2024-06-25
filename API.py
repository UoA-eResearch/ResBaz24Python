#!/usr/bin/env python3

import os
from typing import Annotated
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

df = pd.read_csv("questions.csv", index_col=0)

app = FastAPI(root_path="/resbaz24")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def upload_answer(question: int, answer: str, participant_name: str):
  if answer != df.answer[question]:
    return "👎"
  pd.DataFrame([{"timestamp": datetime.now(), "participant_name": participant_name, "question": question, "answer": answer}]).to_csv("answers.csv", mode="a", header=False, index=False)
  return "👍"