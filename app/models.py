from . import db

# Creating db models by taking advantage of already loaded tables in database


class Customer(db.Model):
    __table__ = db.Model.metadata.tables['customers']


class Restaurant(db.Model):
    __table__ = db.Model.metadata.tables['restaurants']


class PurchaseHistory(db.Model):

    __table__ = db.Model.metadata.tables['purchase_history']


class Dish(db.Model):

    __table__ = db.Model.metadata.tables['dishes']


class OpeningHour(db.Model):

    __table__ = db.Model.metadata.tables['opening_hours']
