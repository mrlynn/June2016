from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'vewy vewy secwet'
DB_NAME = 'mug'

DATABASE = MongoClient()['mug']
EVENTS_COLLECTION = DATABASE.events
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True
