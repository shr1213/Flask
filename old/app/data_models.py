import os
import peewee
import datetime

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
database = peewee.SqliteDatabase(PATH("../../ServerTools/database.db"))


class GoldPrice(peewee.Model):

    '''
        price, date, crawling_times, time
    '''
    price = peewee.CharField()
    date = peewee.DateField()
    crawling_times = peewee.IntegerField()
    time = peewee.TimeField()

    class Meta:
        database = database


class App(peewee.Model):

    '''
        app_name, expect_price
    '''
    app_name = peewee.CharField()
    expect_price = peewee.IntegerField()

    class Meta:
        database = database


class AppPrice(peewee.Model):

    '''
        app name, price, date, crawling_times, time
    '''
    app_name = peewee.CharField()
    price = peewee.CharField()
    date = peewee.DateField()
    crawling_times = peewee.IntegerField()
    time = peewee.TimeField()

    class Meta:
        database = database
