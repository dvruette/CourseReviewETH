from flask import Flask, stream_template, request
from thefuzz import fuzz

from all_courses import COURSES

app = Flask(__name__)

@app.route("/")
def index():
    course = request.args.get("course", None)
    results = []
    if course:
        query = course.lower()
        scores = sorted([(fuzz.ratio(query, course), course) for course in COURSES], reverse=True)
        results = [course for _, course in scores[:5]]
    return stream_template("index.jinja", name="world", courses=results, course=course)