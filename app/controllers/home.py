# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')
