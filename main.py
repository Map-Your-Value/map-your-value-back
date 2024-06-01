from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feature(BaseModel):
    name: str
    select: bool
    # rank: str {high, medium, low}

class rankFeatureList(BaseModel):
    features: List[Feature]




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





@app.get("/")
def read_root():
    return {"Hello": "World"}


# POST /search
# "website": {"www.quivr.com"}

@app.post("/search/")
def searchWebsite(search: str):

    # do IA website to summary + all features

    return {
        "search": search,
        "summary":"Quivr is an open-source platform designed to create \"second brains\" powered by AI. It serves as a unified search engine that integrates and connects various documents, tools, and databases, enabling efficient knowledge discovery and improved search relevance.",
        "features": [
            {"name": "brains", "select": True},
            {"name": "message credits/month", "select": True},
            {"name": "models", "select": True},
            {"name": "storage", "select": True},
            {"name": "in-app chat support", "select": True},
            {"name": "priority email support", "select": True},
            {"name": "custom integrations", "select": True},
            {"name": "premium support", "select": True},
            {"name": "integrations", "select": True},
            {"name": "data syncing", "select": True},
            {"name": "chat history", "select": True},
            {"name": "Quivr Studio", "select": True},
            {"name": "analytics", "select": True},
            {"name": "role-based access control", "select": True},
            {"name": "brains as agents", "select": True},
            {"name": "SSO (Single Sign-On)", "select": True},
            {"name": "SAML", "select": True},
            {"name": "bring your own cloud deployment options", "select": True},
            {"name": "community support", "select": True},
            {"name": "API status update", "select": True},
            {"name": "priority mail support", "select": True},
            {"name": "enterprise support (SLA)", "select": True},
            {"name": "whitelabel", "select": True},
            {"name": "designated customer success team", "select": True},
            {"name": "onboarding support", "select": True},
            {"name": "private slack channel", "select": True}
        ]
        }


# filter by ranking {"High","Medium","Low"} and select True False

# POST /filter/feature
@app.post("/filter/feature")
def filterSearchByFeatures(search: str, summary: str, features: rankFeatureList):

    return {"Hello": "World"}





# filter by ranking {"High","Medium","Low"} and select True False

# POST /filter/competitor
@app.post("/filter/competitor")
def filterSearchByCompetitor(search: str, summary: str, features: rankFeatureList, competitor: rankCompetitorList):

    return {"Hello": "World"}




# /POST /competitor
@app.post("/competitor")
def searchCompetitor(search: str):# , features: rankFeatureList, competitor: rankCompetitorList):
    

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
