from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from werkzeug.exceptions import abort
import requests
import json

from starter.views.auth import login_required
from starter.database import db

blueprint = Blueprint('github', __name__, url_prefix='/github')

@blueprint.route('/')
def index():
    params = {}
    url = ''
    if g.user is None:
        flash('Please sign in with your GitHub account.', 'info')
        url = 'https://api.github.com/users/octocat/starred'
    else:
        params = { 'access_token': session['access_token'] }
        url = 'https://api.github.com/user/starred'

    results = requests.get(url, params=params)

    return render_template('github/index.html', repos=results.json())

@blueprint.route('/search')
def search():
    params = { 'q': search }
    search = request.args.get('query')
    if search is None or search == '':
        return redirect(url_for('github.index'))
    if 'access_token' in session:
        params.access_token = session['access_token']

    url = 'https://api.github.com/search/repositories'

    response = requests.get(url, params=params)
    results = response.json()

    return render_template('github/index.html', repos=results['items'])

@blueprint.route('/star', methods=['POST'])
def star():
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.')
        return '', 404

    full_name = request.form['full_name']
    url = 'https://api.github.com/user/starred/{}'.format(full_name)
    params = { 'access_token': session['access_token'] }
    response = requests.delete(url, params=params)

    return redirect(url_for('github.index'))
