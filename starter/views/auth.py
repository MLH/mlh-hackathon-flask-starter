import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

import requests
import json

from starter.database import get_db

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('public.index'))

        flash(error)

    return render_template('auth/login.html')

@blueprint.route('/github/login')
def githubLogin():
    url = 'https://github.com/login/oauth/authorize?client_id={}&client_secret={}'
    github_oauth_url = url.format(
        current_app.config['GITHUB_CLIENT_ID'],
        current_app.config['GITHUB_CLIENT_SECRET'],
    )
    return redirect(github_oauth_url)

@blueprint.route('/github/register')
def githubRegister():
    url = 'https://github.com/login/oauth/authorize?client_id={}&client_secret={}'
    github_oauth_url = url.format(
        current_app.config['GITHUB_CLIENT_ID'],
        current_app.config['GITHUB_CLIENT_SECRET'],
    )
    return redirect(github_oauth_url)

@blueprint.route('/github/callback', methods=('GET', 'POST'))
def githubCallback():
    if 'code' in request.args:
        url = 'https://github.com/login/oauth/access_token'
        payload = {
            'code': request.args['code'],
            'client_id': current_app.config['GITHUB_CLIENT_ID'],
            'client_secret': current_app.config['GITHUB_CLIENT_SECRET'],
        }
        headers = {'Accept': 'application/json'}
        r = requests.post(url, params=payload, headers=headers)
        response = r.json()
        # get access_token from response and store in session
        if 'access_token' in response:
            session['access_token'] = response['access_token']
        else:
            flash('Could not authorize your request. Oh dear.')
        return redirect(url_for('public.index'))

    return '', 404

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('public.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.access_token is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
