import json
from datetime import datetime
from dataclasses import dataclass
import re

import requests
from flask import Flask, stream_template, request, redirect
from flask_oidc import OpenIDConnect
from thefuzz import fuzz

from courses import get_courses

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': "secret",
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
})
oidc = OpenIDConnect(app)


COURSES = get_courses()
print(f"Loaded {len(COURSES)} courses")


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
    if any(result[key] is None for key in result):
        return None

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

def find_course(course_number: str):
    if not course_number:
        return None
    matches = [course for course in COURSES if course["number"] == course_number]
    if len(matches):
        return matches[0]
    return None


@app.route('/add', defaults={'course_number': None})
@app.route('/add/<course_number>')
@oidc.require_login
def add(course_number: str):
    courses = sorted(COURSES, key=lambda x: x["name"])
    course = find_course(course_number)

    year, month = datetime.now().year, datetime.now().month
    year = year - 2000 if year > 2000 else year - 1900
    semesters = []
    if month > 6:
        semesters.append(f"HS{year}")
    semesters.append(f"FS{year}")
    for i in range(1, 6):
        semesters.append(f"HS{year - i}")
        semesters.append(f"FS{year - i}")

    default_semester = semesters[1] if len(semesters) > 1 else ""

    rating = Rating(0, 0, 0, 0, 0)

    return stream_template("add.jinja", semesters=semesters, default_semester=default_semester, courses=courses, course=course, rating=rating)

@app.route("/")
def index():
    query = request.args.get("query", "")
    results = []
    if query:
        exact_match = re.search(r"[A-Z0-9]{3}-[A-Z0-9]{4}-[A-Z0-9]{3}", query)
        if exact_match:
            return redirect(f"/courses/{exact_match.group(0)}")
        scores = sorted([(fuzz.ratio(query.lower(), f"{course['number']} {course['name']}".lower()), course) for course in COURSES], reverse=True, key=lambda x: x[0])
        results = [course for _, course in scores[:5]]
    sorted_courses = sorted(COURSES, key=lambda x: x["name"])
    return stream_template("index.jinja", courses=sorted_courses, search_results=results, query=query)


@app.route("/courses/<course_number>")
def course(course_number: str):
    course = find_course(course_number)
    rating = None
    reviews = None

    if course:
        rating = get_ratings(course_number)
        reviews = get_reviews(course_number)

    return stream_template("course.jinja", rating=rating, reviews=reviews, course=course)


@app.route("/all")
def all():
    courses = sorted(COURSES, key=lambda x: x["name"])
    return stream_template("all.jinja", courses=courses)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
