from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy


# this methos is responsible for configuring  the connection to the db

def get_db():
    picumo_db = current_app.config['PICUMO_DB_URI']
    client = MongoClient(picumo_db)
    return client.picumo


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def test_connection():
    return dumps(db.collection_names())


def collection_stats(collection_nombre):
    return dumps(db.command('collstats', collection_nombre))

# -----------------Careers-------------------------


def create_career(json):
    return str(db.carreras.insert_one(json).inserted_id)


def retrieve_career_by_id(career_id):
    query = {'_id': ObjectId(career_id)}

    return dumps(db.carreras.find_one(query))


def update_career(career):
    # This function only update career's name and description
    query = {'_id': ObjectId(career['id'])}
    data = {'$set': {'nombre': career['nombre'], 'descripcion': career['descripcion']}}
    return str(db.carreras.update_one(query, data).modified_count)


def delete_career_by_id(career_id):
    query = {'_id': ObjectId(career_id) }
    return str(db.carreras.delete_one(query))


# Operator class
def retrieve_careers(skip, limit):
    return dumps(db.careers.find({}).skip(int(skip)).limit(int(limit)))


def add_course(json):
    return str('Missing to implement')


def delete_course_of_career(json):
    return str('Missing to implement')

# -----------------Course-------------------------


def create_course(json):
    return str('Missing to implement')


def retrieve_course_by_id(id_course):
    return str('Missing to implement')


def update_course(course):
    # This function only update course's name, description and classes
    return str('Missing to implement')


def delete_course_by_id(course_id):
    return str('Missing to implement')


def retrieve_course_by_id_projection(id_course, projection=None):
    return str('Missing to implement')


def retrieve_course_by_name(name):
    return str('Missing to implement')
