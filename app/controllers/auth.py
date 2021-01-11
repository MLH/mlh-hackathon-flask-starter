# -*- coding: utf-8 -*-
import functools, json, requests

from flask import flash, redirect, render_template, request
from flask import Blueprint, session, url_for, g

from app.models.user import User
from app.settings import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from app.services.github import GitHub

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login/github')
def githubLogin():
    github = GitHub(GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET)
    return redirect(github.authorization_url(scope='public_repo'))

@blueprint.route('/callback/github', methods=('GET', 'POST'))
def githubCallback():
    if 'code' not in request.args:
        return '', 500

    # Fetch user from GitHub OAuth and store in session
    github = GitHub(GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET)
    access_token = github.get_token(request.args['code'])

    if access_token is None:
        flash('Could not authorize your request. Please try again.', 'danger')
        return '', 404

    user = User.find_or_create_from_token(access_token)

    session['access_token'] = access_token
    session['user_id'] = user.id

    return redirect(url_for('home.index'))

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))

@blueprint.before_app_request
def get_current_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()
