from datetime import datetime
from flask import render_template, redirect, url_for, session, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User, Role
from ..email import send_email
from config import Config


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/clear')
def clear():
    session['name'] = None
    session['known'] = False
    return redirect(url_for('.user'))


@main.route('/user/', methods=['GET', 'POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed your name')

        session['name'] = form.name.data
        return redirect(url_for('.user'))
    return render_template('user.html', form=form, name=session.get('name'))

