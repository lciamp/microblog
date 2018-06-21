from config import Config
from flask import render_template, current_app
from flask_mail import Message
from threading import Thread
from app import mail


# asynchronous email
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# functions for sending an email
def send_email(to, subject, template, **kwargs):
    msg = Message(Config.FLASKY_MAIL_SUBJECT_PREFIX + subject,
                  sender=Config.FLASKY_MAIL_SENDER,
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[current_app._get_current_object(), msg])
    thr.start()
    return thr
