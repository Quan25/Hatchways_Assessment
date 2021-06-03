from flask import Flask, jsonify, make_response, request
import requests
import helper
from json import JSONDecoder

app = Flask(__name__)

BASE_URL = "https://api.hatchways.io/assessment/blog/posts?tag="
SORT_VALID_ARGS = ["id", "reads", "likes", "popularity"]
DIRECTION = ["asc", "desc"]


@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/api/ping", methods=['GET'])
def ping():
    ping_result = jsonify(
        Success=True
    )
    return make_response(ping_result, 200)

@app.route('/api/posts', methods=['GET'])
def get_post():
    sortBy = "id"
    direction = "asc"
    order = False
    tags = request.args.get('tags')
    if (request.args.get('sortBy')):
        sortBy = request.args.get('sortBy')
    if(request.args.get('direction')):
        direction = request.args.get('direction')

    if (not tags):
        error = jsonify(
            error = "Tags parameter is required"
        )
        return make_response(error, 400)

    urls = [(BASE_URL + tag) for tag in tags.split(',')]
    result = helper.threading(urls)

    if direction not in DIRECTION:
        error = jsonify(
            error = "direction parameter is invalid"
        )
        return make_response(error, 400)
    if sortBy not in SORT_VALID_ARGS:
        error = jsonify(
            error = "sortBy parameter is invalid"
        )
        return make_response(error, 400)

    if direction == "desc":
        order = True
    result = helper.sortList(result, sortBy, order)
    data = jsonify(
        posts = result
    )
    return make_response(data, 200)
