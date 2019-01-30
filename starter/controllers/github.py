from flask import redirect, render_template, request
from flask import Blueprint, flash, url_for, session

from starter.controllers.auth import login_required
from starter.database import db
from starter.services.github import GitHub

blueprint = Blueprint('github', __name__, url_prefix='/github')

@blueprint.route('/')
def index():
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'info')
        return render_template('github/index.html')

    starred_repos = GitHub.get_starred_repos(session['access_token'])
    return render_template('github/index.html', repos=starred_repos)

@blueprint.route('/search')
def search():
    search = request.args.get('query')

    if search is None or search == '':
        flash('Please include a repo name you want to search for.')
        return redirect(url_for('github.index'))
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'error')
        return redirect(url_for('github.index'))

    repos = GitHub.search_repos(session['access_token'], search )
    return render_template('github/index.html', repos=repos['items'])

@blueprint.route('/star', methods=['POST'])
def star():
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'error')
        return redirect(url_for('github.index'))

    GitHub.unstar_repo(session['access_token'], request.form['full_name'])

    return redirect(url_for('github.index'))
