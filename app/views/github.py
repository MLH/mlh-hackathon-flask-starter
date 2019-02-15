# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from flask import Blueprint, flash, url_for, session

from app.views.auth import login_required
from app.services.github import GitHub
from app.extensions import markdown

blueprint = Blueprint('github', __name__)

@blueprint.route('/fetching')
def fetching():
    if not 'access_token' in session:
        flash('This page needs an authenticated user. Please sign in with your GitHub account.', 'warning')
        return render_template('github/index.html')

    github = GitHub(access_token=session['access_token'])

    starred_repos = github.get('/user/starred')
    return render_template('github/fetching.html', repos=starred_repos[:5])

@blueprint.route('/searching')
def searching():
    if not 'access_token' in session:
        flash('This page needs an authenticated user. Please sign in with your GitHub account.', 'warning')
        return render_template('github/index.html')

    github = GitHub(access_token=session['access_token'])

    starred_repos = github.get('/user/starred')
    return render_template('github/searching.html', repos=starred_repos[:5])

@blueprint.route('/search')
def search():
    search = request.args.get('query')

    if search is None or search == '':
        flash('Please include a repo name you want to search for.', 'danger')
        return redirect(url_for('github.index'))
    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'danger')
        return redirect(url_for('github.index'))

    github = GitHub(access_token=session['access_token'])

    repos = github.get('/search/repositories', { 'q': search } )
    return render_template('github/index.html', repos=repos['items'])

@blueprint.route('/star', methods=['POST'])
def star():
    repo = request.form['full_name']

    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'danger')
        return redirect(url_for('github.index'))

    github = GitHub(access_token=session['access_token'])
    github.delete('/user/starred/' + repo)

    return redirect(url_for('github.index'))
