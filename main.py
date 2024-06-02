from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from time import sleep

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
    Company_Card: str


class rankCompetitorList(BaseModel):
    competitors: List[descriptionOfACompany]


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/competitor")
def searchCompetitor(search: str):
    sleep(1)  # Adding a sleep of 10 seconds
    # out = analyse_company(search)
    # competitors = []

    # for i in out["competitors"]:
    #    i["Company_Card"] = ""

    # for i in out["competitors"]:
    #    competitors.append(descriptionOfACompany.model_validate(i, from_attributes=True, strict=False))

    # for i in competitors:
    #    if i.Competitor == "Otter.ai":
    #        with open("./extraction/company_fact_card/otter.txt", "r") as f:
    #            i.Company_Card = f.read()
    #    if i.Competitor == "Zoom IQ":
    #        with open("./extraction/company_fact_card/zoom.txt", "r") as f:
    #            i.Company_Card = f.read()

    # return rankCompetitorList(competitors=competitors)

    demo_data = rankCompetitorList(competitors=[
        descriptionOfACompany(
            Competitor="Otter.ai",
            Descriptive_summary="Otter.ai is an AI-powered transcription service that records audio, writes notes, captures slides, and generates summaries.",
            Strengths=["Widely known in the transcription market", "strong brand recognition",
                       "offers real-time transcription."],
            Weaknesses=["Primary focus on transcription",
                        "less emphasis on meeting insights and integrations compared to tl;dv."],
            Proximity_score=5,
            Proximity_Explanation="Very similar core functionality in terms of transcription and summarization, but tl;dv offers a broader range of features like integrations and meeting insights.",
            Crunchbase_Link="https://rb.gy/me6k4",
            Company_Card="Otter.ai - AI Meeting Assistance Platform\n1. Company Name and Mission:\n\nOtter.ai is an AI-powered meeting assistance platform with the primary mission to make meetings better and more productive by leveraging advanced AI technology for real-time transcription, note-taking, and meeting analysis.\n\n2. Technology Services and Integrations:\n\nOtter.ai provides the following core services:\n\nReal-time AI Transcription: Automatically transcribes meetings in various languages with high accuracy, directly within platforms like Zoom, Google Meet, and Microsoft Teams."
        ),
        descriptionOfACompany(
            Competitor="Gong",
            Descriptive_summary="Gong is a revenue intelligence platform that captures customer interactions, analyzes them using AI, and provides insights to improve sales performance.",
            Strengths=["Strong focus on revenue intelligence and sales performance improvement",
                       "robust analytics and reporting features."],
            Weaknesses=["More expensive and feature-rich than tl;dv",
                        "may be overkill for businesses solely looking for meeting note-taking."],
            Proximity_score=3,
            Proximity_Explanation="Overlaps with tl;dv in terms of meeting insights and sales coaching, but Gong is a more comprehensive and expensive solution.",
            Crunchbase_Link="https://rb.gy/0z0q7",
            Company_Card=""
        ),
        descriptionOfACompany(
            Competitor="Chorus.ai (acquired by Zoom)",
            Descriptive_summary="Chorus, now part of Zoom, is a conversation intelligence platform that helps sales teams improve their performance through AI-powered analysis of calls and meetings.",
            Strengths=["Seamless integration with Zoom", "strong focus on sales coaching and performance improvement."],
            Weaknesses=["May lack the breadth of integrations offered by tl;dv", "primarily focused on sales teams."],
            Proximity_score=2,
            Proximity_Explanation="Similar to Gong, Chorus focuses on conversation intelligence for sales, overlapping with some of tl;dv's features but with a narrower focus.",
            Crunchbase_Link="https://rb.gy/m9lbey",
            Company_Card=""
        ),
        descriptionOfACompany(
            Competitor="Fireflies.ai",
            Descriptive_summary="Fireflies.ai is an AI meeting assistant that transcribes meetings, generates summaries, and helps with action items.",
            Strengths=["Affordable pricing", "user-friendly interface", "good integration with various platforms."],
            Weaknesses=["May not be as feature-rich as tl;dv in terms of meeting insights and language support."],
            Proximity_score=2,
            Proximity_Explanation="Direct competitor to tl;dv with a similar feature set, but tl;dv offers more advanced features and broader language support.",
            Crunchbase_Link="https://rb.gy/w2w89",
            Company_Card=""
        ),
        descriptionOfACompany(
            Competitor="Avoma",
            Descriptive_summary="Avoma is a conversation intelligence platform that helps sales teams record, transcribe, analyze, and automate meeting workflows.",
            Strengths=["Strong focus on sales automation and workflow integration",
                       "offers features like meeting scheduling and CRM integration."],
            Weaknesses=["May not be as strong as tl;dv in AI-powered insights and multilingual support."],
            Proximity_score=1,
            Proximity_Explanation="Shares some features with tl;dv, particularly in meeting transcription and sales automation, but tl;dv has a stronger focus on AI and multilingual capabilities.",
            Crunchbase_Link="https://rb.gy/9zswg",
            Company_Card=""
        ),
        descriptionOfACompany(
            Competitor="Sembly.ai",
            Descriptive_summary="Sembly.ai is an AI meeting assistant that provides real-time transcription, meeting summaries, and insights.",
            Strengths=["Real-time transcription capabilities", "offers integrations with popular productivity tools."],
            Weaknesses=["May not be as widely known as some competitors",
                        "may lack the depth of integrations offered by tl;dv."],
            Proximity_score=1,
            Proximity_Explanation="Very similar to tl;dv in terms of core functionality and value proposition, but tl;dv boasts a wider range of integrations.",
            Crunchbase_Link="https://rb.gy/q9f8p",
            Company_Card=""
        ),
        descriptionOfACompany(
            Competitor="MeetGeek.ai",
            Descriptive_summary="MeetGeek.ai is an AI-powered meeting platform that helps teams record, transcribe, analyze, and share key meeting insights.",
            Strengths=["Strong focus on meeting intelligence and collaboration",
                       "offers features like shared meeting notes and action items."],
            Weaknesses=["May not be as strong as tl;dv in terms of integrations and language support."],
            Proximity_score=4,
            Proximity_Explanation="Direct competitor to tl;dv with a strong focus on meeting intelligence, but tl;dv offers broader integration capabilities and language support.",
            Crunchbase_Link="https://rb.gy/9x9w4",
            Company_Card=""
        )
    ])
    return demo_data
