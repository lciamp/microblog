from datetime import datetime
from flask import render_template, redirect, url_for, session, flash
from . import main
from flask_login import login_required
from ..models import Permission
from ..decorators import admin_required, permission_required
from .forms import NameForm
from .. import db
from ..models import User, Role
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "for administrators!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "for comment mods!"


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)