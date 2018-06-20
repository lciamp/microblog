# a if condition else b

'''
name_for_uid = {
	1: 'Lou', 
	2: 'Hudson', 
	3: 'Bean'
}

def greeting(id):
	return ('Hello %s!' % name_for_uid.get(id)) if name_for_uid.get(id, False) else 'Not Registered User!'

#print(greeting(45))

#print(greeting(1))
x = 0
print(x)
while x != 4:
	x = int(input('Enter a user id:\n'))

	print(greeting(x))
'''

## classes in a package
from flask import Flask
from hello import mail
from flask_mail import Message
import pkgutil
import sys


# send mail test:
def send_mail(subject, body):
    msg = Message(subject, sender='louis.ciampanelli@gmail.com', recipients=['l.ciamp@me.com'])
    msg.body = body
    msg.html = '<b>' + body + '</b>'

    try:
        mail.send(msg)
        return 'Mail Sent'
    except:
        return 'Mail Failed'


'''
def explore_package(module_name):
    loader = pkgutil.get_loader(module_name)
    for sub_module in pkgutil.walk_packages([loader.filename]):
        _, sub_module_name, _ = sub_module
        qname = module_name + "." + sub_module_name
        print(qname)
        explore_package(qname)


explore_package('flask.signals')
'''
