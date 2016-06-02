#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python TweetFromMongo.py

import time, sys, datetime
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_debugtoolbar import DebugToolbarExtension
from TwitterAPI import TwitterAPI


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'uqtaCC3G0weEMMRdxuogmtJkA'
CONSUMER_SECRET = 'rtj0YLpLBbNlZoc6YXEPXolF75SkDSoCQhTiHhaypnizALho6w'
ACCESS_KEY = '703708784171032576-joXLzsQQW518NTbkj5H0lSsC9rPTOLv'
ACCESS_SECRET = '1wosJJ9ToqF2MPJLQTnk9CCghGWrXePBdBOK92VBkaOP0'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)


client = MongoClient('localhost',27017)
db = client.mug

dt  = datetime.datetime
now = dt.now()

# This gives timedelta in days & seconds
dt(year=2016,month=06,day=22) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute)

print dt(year=2016,month=06,day=22) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute)
diff = dt(year=2016,month=06,day=22) - dt(year=now.year, month=now.month, day=now.day)

print diff.days

_events = db.events.find()

data = [item for item in _events]

for d in data:
	msgs = d['messages']
	for m in msgs:
		if diff.days == m['daysleft']:
			status = m['message'] 
			image = m['image']
			file = open(image, 'rb')
			pdata = file.read()
			r = api.request('media/upload', None, {'media': pdata})
			print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE')
			print r.status_code

			if r.status_code == 200:
				media_id = r.json()['media_id']
				r = api.request('statuses/update', {'status':status, 'media_ids':media_id})
				print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE')
