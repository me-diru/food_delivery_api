
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # basic configurations required
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something_complicated'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data/prod_application.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
