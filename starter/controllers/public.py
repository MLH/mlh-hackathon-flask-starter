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

@blueprint.route('/user-guide')
def user_guide():
    with open('starter/docs/USER_GUIDE.md', 'r') as input_file:
        text = input_file.read()
        headers = { 'Content-Type': 'text/plain' }
        url = 'https://api.github.com/markdown/raw'
        response = requests.post(url, data=text, headers=headers)
        data = response.content.decode('utf-8')

        return render_template('home/index.html', body=data)


@blueprint.route('/getting-started')
def getting_started():
    with open('starter/docs/GETTING_STARTED.md', 'r') as input_file:
        text = input_file.read()
        headers = { 'Content-Type': 'text/plain' }
        url = 'https://api.github.com/markdown/raw'
        response = requests.post(url, data=text, headers=headers)
        data = response.content.decode('utf-8')

        return render_template('home/index.html', body=data)
