from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class descriptionOfACompany(BaseModel):
    id: int
    name: str
    website: str
    summary: str
    features: list[str]
    uniqueVisitor: int
    # rank: str {high, medium, low}
    # select: bool
    # more columns to add here 

class rankCompetitorList(BaseModel):
    competitors: List[descriptionOfACompany]


# /POST /competitor
@app.get("/competitor")
def searchCompetitor(search: str):

    # Get oll 

    # Define the list of competitors
    

    competitors = [
        descriptionOfACompany(
            id=1,
            name="parcha",
            website="www.parcha.com",
            summary="summary of parcha here",
            features=["features1", "features2"],
            uniqueVisitor=1000
        ),
        descriptionOfACompany(
            id=2,
            name="simular",
            website="www.simular.ai/",
            summary="summary of simular here",
            features=["features1", "features2"],
            uniqueVisitor=500
        )
    ]


    return rankCompetitorList(competitors=competitors)
