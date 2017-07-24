# -*- coding: utf8 -*-
from unittest import TestCase

from flask import Flask

from flask_table import Page
from flask_table.model import Column, Model
from flask_table.table import TableBase
from flask_table.view import TableView

app = Flask(__name__)


class _User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class User(Model):
    name = Column(default=None)
    email = Column(default=None)

    @classmethod
    def get_result_set(cls):
        users = [_User("wanghao01", 'wanghao01@qq.com')]
        rv = []
        instance = cls()
        for user in users:
            instance.name = user.name
            instance.email = user.email
            rv.append(instance)
        return rv


class UserTable(TableBase):
    model = User


class UserView(TableView):
    table = UserTable


class TestBase(TestCase):
    def setUp(self):
        self.model = User
        self.table = UserTable
        self.view = UserView
        self.app = app
        self.page = Page(app)
        self.page.add_view(UserView)
