#!/usr/bin/env python3

from fastapi import FastAPI
import pandas as pd

df = pd.read_csv("questions.csv", index_col=0)

app = FastAPI()

@app.get("/")
def get():
  return pd.read_csv("answers.csv", names=["timestamp", "participant_name", "question", "answer", "is_correct"]).to_dict(orient="records")

@app.post("/")
def post(question: int, answer: str, participant_name: str):
  is_correct = answer == df.answer[question]
  pd.DataFrame([{
    "timestamp": pd.Timestamp.now(),
    "participant_name": participant_name,
    "question": question,
    "answer": answer,
    "is_correct": is_correct
  }]).to_csv("answers.csv", mode="a", header=False, index=False)

  if is_correct:
    return "👍"
  else:
    return "👎"