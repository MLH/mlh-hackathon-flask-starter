import functools

from flask import flash, redirect, render_template, request
from flask import Blueprint, session, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash

import requests
import json

from starter.extensions import db
from starter.models.user import User
from starter.settings import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

github_oauth_url = 'https://github.com/login/oauth/authorize?client_id={}&client_secret={}&scope={}'.format(
    GITHUB_CLIENT_ID,
    GITHUB_CLIENT_SECRET,
    'public_repo'
)

@blueprint.route('/github/login')
def githubLogin():
    return redirect(github_oauth_url)

@blueprint.route('/github/register')
def githubRegister():
    return redirect(github_oauth_url)

@blueprint.route('/github/callback', methods=('GET', 'POST'))
def githubCallback():
    if 'code' not in request.args:
        return '', 404

    # fetch access_token from GitHub OAuth and store in session
    access_token = fetch_access_token(request.args['code'])
    session['access_token'] = access_token

    data = fetch_github_user(access_token)
    user = find_or_create_user(data)
    session['user_id'] = user.id

    return redirect(url_for('public.index'))

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('public.index'))

@blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()

"""Helper functions"""

def fetch_access_token(code):
    """Fetch GitHub Access Token for GitHub OAuth"""
    url = 'https://github.com/login/oauth/access_token'
    headers = { 'Accept': 'application/json' }
    payload = {
        'code': code,
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
    }

    response = requests.post(url, params=payload, headers=headers)
    data = response.json()

    if not 'access_token' in data:
        # Issue in retrieving GitHub access token
        flash('Could not authorize your request. Please try again.')
        return '', 404

    return data['access_token']

def fetch_github_user(access_token):
    url = 'https://api.github.com/user'
    payload = { 'access_token': access_token }

    response = requests.get(url, params=payload)
    return response.json()

def find_or_create_user(data):
    """Find existing user or create new User instance"""
    instance = User.query.filter_by(username=data['login']).first()

    if not instance:
        instance = User(data['login'], data['avatar_url'], data['id'])
        db.session.add(instance)
        db.session.commit()

    return instance
