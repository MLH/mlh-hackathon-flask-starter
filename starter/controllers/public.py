from flask import Blueprint, flash, render_template, request, session

import requests

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def index():
    with open('README.md', 'r') as input_file:
        text = input_file.read()
        headers = { 'Content-Type': 'text/plain' }
        url = 'https://api.github.com/markdown/raw'
        response = requests.post(url, data=text, headers=headers)
        data = response.content.decode('utf-8')

        return render_template('home/index.html', body=data)

@blueprint.route('/about')
def about():
    # TODO: Create this template
    return render_template('home/index.html')

@blueprint.route('/getting-started')
def getting_started():
    # TODO: Create this template
    return render_template('home/index.html')
