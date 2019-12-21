from flask import Blueprint, request, jsonify
from . import db
import json

bp = Blueprint('careers', __name__, url_prefix='/carreras')


@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def careers_func():
    career_id = request.args.get('id')
    skip = request.args.get('skip')
    limit = request.args.get('limit')

    request_body = request.get_json()
    if request.method == 'POST':
        # Create career
        return jsonify({'_id': db.create_career(request_body)})
    elif request.method == 'PUT':
        # Update career's name and description
        return jsonify({'updated': db.update_career(request_body)})
    elif request.method == 'DELETE' and career_id is not None:
        # Delete a career using a _id 
        return jsonify({'deleted': db.delete_career_by_id(career_id)})
    elif career_id is not None:
        # Get careers by _id
        result = db.retrieve_career_by_id(career_id)
        return jsonify({'career': json.loads(result)})
    else:
        # Get careers
        skip = (skip, 0)[skip is None]
        limit = (limit, 10)[limit is None]
        result = db.retrieve_careers(skip, limit)
        return jsonify({'careers': json.loads(result)})


@bp.route('/agregar-curso', methods=['PUT', 'DELETE'])
def add_course():
    request_body = request.get_json()
    if request.method == 'PUT':
        return jsonify({'updated': json.loads(db.add_course(request_body))})
    elif request.method == 'DELETE':
        return jsonify({'deleted': json.loads(db.delete_course_of_career(request_body))})


@bp.route('/test')
def test_connection():
    return jsonify({'collections': json.loads(db.test_connection())})
