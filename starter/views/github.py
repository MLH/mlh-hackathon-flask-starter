from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from werkzeug.exceptions import abort
import requests
import json

from starter.views.auth import login_required
from starter.extensions import db

blueprint = Blueprint('github', __name__, url_prefix='/github')

@blueprint.route('/')
def index():
    params = {}
    url = 'https://api.github.com/users/octocat/repos'
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.')
    else:
        params = { 'access_token': session['access_token'] }

    results = requests.get(url, params=params)

    return render_template('github/index.html', repos=results.json())

@blueprint.route('/search')
def search():
    params = {}
    search = request.args.get('query')
    if search is None or search == '':
        return redirect(url_for('github.index'))
    if 'access_token' in session:
        params = { 'q': search, 'access_token': session['access_token'] }
    else:
        params = { 'q': search }

    url = 'https://api.github.com/search/repositories'

    response = requests.get(url, params=params)
    results = response.json()

    return render_template('github/index.html', repos=results['items'])

@blueprint.route('/star', methods=['POST'])
def star():
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.')

    return render_template('github/index.html')
