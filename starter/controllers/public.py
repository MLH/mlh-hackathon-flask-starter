from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from starter.controllers.auth import login_required

blueprint = Blueprint('public', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/about')
def about():
    # TODO: Create this template
    return render_template('home/index.html')

@blueprint.route('/getting-started')
def getting_started():
    # TODO: Create this template
    return render_template('home/index.html')
