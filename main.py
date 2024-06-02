from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from extraction.chain import analyse_company

app = FastAPI()


class descriptionOfACompany(BaseModel):
    Competitor: str
    Descriptive_summary: str
    Strengths: List[str] | str
    Weaknesses: List[str] | str
    Proximity_score: int
    Proximity_Explanation: str
    Crunchbase_Link: str


class rankCompetitorList(BaseModel):
    competitors: List[descriptionOfACompany]


# /POST /competitor
@app.get("/competitor")
def searchCompetitor(search: str):
    out = analyse_company("https://tldv.io/")
    competitors = []
    for i in out["competitors"]:
        competitors.append(
            descriptionOfACompany.model_validate(i, from_attributes=True, strict=False)
        )

    return rankCompetitorList(competitors=competitors)
