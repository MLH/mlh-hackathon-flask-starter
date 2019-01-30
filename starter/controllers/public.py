from flask import Blueprint, render_template

from starter.extensions import markdown

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def index():
    with open('README.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)

@blueprint.route('/user-guide')
def user_guide():
    with open('starter/docs/USER_GUIDE.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)

@blueprint.route('/getting-started')
def getting_started():
    with open('starter/docs/GETTING_STARTED.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)
