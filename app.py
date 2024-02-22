import json
from dataclasses import dataclass

import requests
from flask import Flask, stream_template, request
from thefuzz import fuzz

from all_courses import COURSES

app = Flask(__name__)


@dataclass
class Rating:
    recommended: float
    interesting: float
    difficulty: float
    effort: float
    resources: float

@dataclass
class Review:
    review: str
    semester: str

def get_ratings(course_number: str) -> Rating:
    url = f"https://rubberducky.vsos.ethz.ch:1855/rating/{course_number}"
    result = json.loads(requests.get(url).json())[0]
    rating = Rating(
        recommended=result["AVG(Recommended)"],
        interesting=result["AVG(Interesting)"],
        difficulty=result["AVG(Difficulty)"],
        effort=result["AVG(Effort)"],
        resources=result["AVG(Resources)"]
    )
    return rating

def get_reviews(course_number: str) -> list[Review]:
    url = f"https://rubberducky.vsos.ethz.ch:1855/course/{course_number}"
    result = json.loads(requests.get(url).json())
    reviews = [Review(review=review["Review"], semester=review["Semester"]) for review in result]
    return reviews

@app.route("/")
def index():
    course = request.args.get("course", None)
    results = []
    if course:
        query = course.lower()
        scores = sorted([(fuzz.ratio(query, course), course) for course in COURSES], reverse=True)
        results = [course for _, course in scores[:5]]
    return stream_template("index.jinja", courses=results, course=course)

@app.route("/courses/<course_number>")
def course(course_number: str):
    course = None
    rating = None
    reviews = None

    if course_number:
        matches = [course for course in COURSES if course["number"] == course_number]
        if len(matches):
            course = matches[0]
            rating = get_ratings(course_number)
            reviews = get_reviews(course_number)

    return stream_template("course.jinja", rating=rating, reviews=reviews, course=course)

@app.route("/all")
def all():
    courses = sorted(COURSES, key=lambda x: x["name"])
    return stream_template("all.jinja", courses=courses)

if __name__ == "__main__":
    app.run(debug=True)
