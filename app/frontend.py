from app import app

__author__ = 'briandavidfarris@gmail.com'

import json
import random
import string
from apiclient.discovery import build

from flask import Flask
from flask import render_template
from flask import flash
from flask import session
from flask import redirect 
from flask import url_for 

from forms import BlahForm

import httplib2

from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension

APPLICATION_NAME = 'Application Name'

app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
                         for x in xrange(32))

# See the simplekv documentation for details
store = DictStore()

# This will replace the app's session handling
KVSessionExtension(store, app)

# Update client_secrets.json with your Google API project information.
# Do not change this assignment.
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
SERVICE = build('plus', 'v1')

@app.route('/', methods = ['GET', 'POST'])
def index():
  credentials=session.get('credentials')
  if credentials is None:
    return redirect(url_for('login'))
  else:
    # Create a new authorized API client.
    http = httplib2.Http()
    http = credentials.authorize(http)

    thisuser_request = SERVICE.people().get(userId='me')
    thisuser = thisuser_request.execute(http=http)
   
    form = BlahForm()
    if form.validate_on_submit():
      flash('You entered:' + form.text_entry.data + ', boolean_entry=' + str(form.boolean_entry.data)+', date_entry='+form.date_entry.data.isoformat()+', select_entry='+form.select_entry.data+', integer_entry='+str(form.integer_entry.data))
    else:

    return render_template('index.html',
        appname = APPLICATION_NAME,
        thisuser = thisuser,
        form = form) 
 



