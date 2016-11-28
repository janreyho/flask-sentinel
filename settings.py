# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'evedemo')


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
teachers = {
    'item_title': 'user',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    'schema': {
        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            'unique': True,
        },
        'password': {
            'type': 'string',
            'required': True,
        },
        'nickname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }
}

students = {
    'item_title': 'user',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    'schema': {
        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            'unique': True,
        },
        'password': {
            'type': 'string',
            'required': True,
        },
        'nickname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
    }
}

courses = {
    'item_title': 'course',

    # 'additional_lookup': {
    #     'url': 'regex("[\w]+")',
    #     'field': '_id'
    # },

    'schema': {
        'teacherID': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'teachers',
                'embeddable': True
            },
        },
        'studentID': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'students',
                'embeddable': True
            },
        },
        'startTime': {
            'type': 'datetime',
        },
        'duration': {
            'type': 'integer',
        },
        'status': {
            'type': 'string', 
            'allowed': ['created', 'qqcontact', 'prepared','telcontact', 'preHostVisit', 'started', 'completed', 'sendReport', 'preHostVisit', 'closed']
        }
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'students': students,
    'courses': courses,
    'teachers': teachers,
}
