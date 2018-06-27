# /app/main/errors.py

from flask import render_template, request, jsonify
from . import main

# helper function to return json or html

def request_wants_json():
    if 'application/json' in request.headers['Accept']:
        return True
    else:
        return False


# error handlers

@main.app_errorhandler(400)
def bad_request(e):
    if request_wants_json():
        response = jsonify({'error': 'bad request'})
        response.status_code = 400
        response.content_type = 'application/json'
        return response
    msg = {'error': 'bad request', 'code': 400}
    return render_template('error.html', msg=msg), 400


@main.app_errorhandler(401)
def forbidden(e):
    if request_wants_json():
        response = jsonify({'error': 'unauthorized request'})
        response.status_code = 401
        response.content_type = 'application/json'
        return response
    msg = {'error': 'unauthorized request', 'code': 401}
    return render_template('error.html', msg=msg), 401


@main.app_errorhandler(403)
def forbidden(e):
    if request_wants_json():
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        response.content_type = 'application/json'
        return response
    msg = {'error': 'forbidden', 'code': 403}
    return render_template('error.html', msg=msg), 403


@main.app_errorhandler(404)
def page_not_found(e):
    if request_wants_json():
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        response.content_type = 'application/json'
        return response
    msg = {'error': 'page not found', 'code': 404}
    return render_template('error.html', msg=msg), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request_wants_json():
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        response.content_type = 'application/json'
        return response
    msg = {'error': 'internal server error', 'code': 500}
    return render_template('error.html', msg=msg), 500

