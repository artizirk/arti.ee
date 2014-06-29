import datetime
from flask import url_for
from .app import db


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class User(db.Document):
    password = db.StringField(max_length=255, required=True)
    username = db.StringField(max_length=255, required=True)
    email = db.EmailField(max_length=255, required=True)
    salt = db.StringField(required=True)
    registered_on = db.DateTimeField(default=datetime.datetime.now, required=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.email)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-registered_on', 'email', 'username'],
        'ordering': ['-registered_on']
    }
