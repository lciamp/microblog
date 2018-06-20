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
    form = NameForm()
    if form.validate_on_submit():
        print('index page used from blueprint')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role=Role.query.filter_by(name='User').first())
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if Config.FLASKY_ADMIN:
                print('Attempting to send email')
                try:
                    send_email(Config.FLASKY_ADMIN, 'New User', 'mail/newuser', user=user)
                    print('email sent')
                except:
                    print('email failed')
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


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

