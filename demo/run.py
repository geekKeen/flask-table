# -*- coding: utf8 -*-
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_table import TableView, Page
from flask_table.table import TableBase
from flask_table.model import Column, Model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s" % os.path.join(os.path.abspath(os.path.curdir), 'test.db')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
page = Page(app)


class UserDB(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<User %s>" % self.name


class User(Model):
    name = Column(default=None)
    email = Column(default=None)

    @classmethod
    def get_result_set(cls):
        users = UserDB.query.all()
        rv = []
        for user in users:
            instance = cls()
            instance.name = user.name
            instance.email = user.email
            rv.append(instance)
        return rv


class UserTable(TableBase):
    model = User

    columns = ('name', 'email')
    column_labels = {
        'name': u"姓名",
        'email': u"邮件",
    }


class UserView(TableView):
    table = UserTable


page.add_view(UserView)

if __name__ == '__main__':
    app.run(debug=True)
