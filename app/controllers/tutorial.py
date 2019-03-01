# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from flask import g, Blueprint, flash, url_for, session

from app.services.github import GitHub

blueprint = Blueprint('tutorial', __name__, url_prefix='/tutorial')

@blueprint.route('/requesting')
def requesting():
    search = request.args.get('query', '')
    if not 'access_token' in session:
        flash('This tutorial needs an authenticated user to make the request. Please sign in with your GitHub account.', 'danger')
        return render_template('tutorial/requesting.html')

    github = GitHub(access_token=session['access_token'])
    results1 = github.get('/user/starred')
    results2 = github.get('/search/repositories', { 'q': search } )
    results2 = results2.get('items', [])

    return render_template('tutorial/requesting.html',
        tutorial1 = results1[:5],
        tutorial2 = results2[:5],
        query = search
    )

@blueprint.route('/star', methods=['POST'])
def star():
    repo = request.form['full_name']

    if not 'access_token' in session:
        flash('Please sign in with your GitHub account.', 'danger')
        return redirect(url_for('github.fetching'))

    github = GitHub(access_token=session['access_token'])
    github.delete('/user/starred/' + repo)

    return redirect(url_for('tutorial.fetching'))
