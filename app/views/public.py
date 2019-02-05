from flask import Blueprint, render_template

from app.extensions import markdown

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def index():
    with open('README.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)

@blueprint.route('/user-guide')
def user_guide():
    with open('docs/USER_GUIDE.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)

@blueprint.route('/contributing')
def contributing():
    with open('docs/CONTRIBUTING.md', 'r') as input_file:
        text = input_file.read()
        content = markdown.render(text)
        return render_template('home/index.html', body=content)
