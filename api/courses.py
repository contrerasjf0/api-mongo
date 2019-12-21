from flask import Blueprint, request, jsonify
from . import db
import json

bp = Blueprint('courses', __name__, url_prefix='/cursos')


@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def courses_func():
    course_id = request.args.get('id')
    request_body = request.get_json()
    if request.method == 'POST':
        # Create course
        return jsonify({"_id": db.create_course(request_body)})
    elif request.method == 'PUT':
        # Update career's name and description
        return jsonify({'updated': db.update_course(request_body)})
    elif request.method == 'DELETE' and course_id is not None:
        # Delete a course using _id
        return jsonify({'deleted': db.delete_course_by_id(course_id)})
    elif course_id is not None:
        # Get Course by _id
        result = db.retrieve_course_by_id(course_id)
        return jsonify({"clase": json.loads(result)})


@bp.route('/porNombre', methods=['POST'])
def courses_by_name():
    request_body = request.get_json()
    result = db.retrieve_course_by_name(request_body["name"])
    return jsonify({"courses": json.loads(result)})


@bp.route('/stats')
def stats_collection():
    return jsonify({"collections": json.loads(db.collection_stats("courses"))})