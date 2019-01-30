import functools

from flask import flash, redirect, render_template, request
from flask import Blueprint, session, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash

import requests
import json

from starter.database import db
from starter.models.user import User
from starter.settings import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from starter.services.github import GitHub

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

github_oauth_url = 'https://github.com/login/oauth/authorize?client_id={}&client_secret={}&scope={}'.format(
    GITHUB_CLIENT_ID,
    GITHUB_CLIENT_SECRET,
    'public_repo'
)

@blueprint.route('/github/login')
def githubLogin():
    return redirect(github_oauth_url)

@blueprint.route('/github/callback', methods=('GET', 'POST'))
def githubCallback():
    if 'code' not in request.args:
        return '', 500

    github = GitHub(GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET)
    # Fetch user from GitHub OAuth and store in session
    access_token = github.get_token(request.args['code'])
    user = User.find_or_create_from_token(access_token)

    session['access_token'] = access_token
    session['user_id'] = user.id

    return redirect(url_for('public.index'))

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('public.index'))

@blueprint.before_app_request
def get_current_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
