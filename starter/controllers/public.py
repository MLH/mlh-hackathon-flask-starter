from flask import Blueprint, flash, render_template, request, session

from starter.views.auth import login_required

import requests

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def index():
    # params = { 'access_token': session['access_token'] }
    headers = { 'Content-Type': 'application/json' }
    text = '# Introduction\n\n This is a new document. Let\'s see what we can do.'
    url = 'https://api.github.com/markdown/raw'
    response = requests.post(url, data=text, headers=headers)

    return render_template('home/index.html', body=response.content)

@blueprint.route('/about')
def about():
    # TODO: Create this template
    return render_template('home/index.html')

@blueprint.route('/getting-started')
def getting_started():
    # TODO: Create this template
    return render_template('home/index.html')
