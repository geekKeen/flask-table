# -*- coding: utf8 -*-
import os

from flask.views import View
from flask import Blueprint

from .table import TableBase
from .utils import camel_to_snake_case

template_folder = os.path.join(os.path.curdir, 'templates')


class ViewMeta(type):
    def __init__(cls, classname, base, fields):
        super(ViewMeta, cls).__init__(classname, base, fields)
        cls.name = cls.name = camel_to_snake_case(classname)
        cls.rule = "/%s/" % cls.name


class TableView(View):
    """
    将 flask-table 的请求直接与Flask 的请求对接
    """
    __metaclass__ = ViewMeta

    methods = ['GET']
    table = TableBase

    @classmethod
    def create_blueprint(cls, page):
        blueprint = Blueprint(cls.name, __name__, template_folder=template_folder, url_prefix=page.url_prefix)
        blueprint.add_url_rule(cls.rule, view_func=cls.as_view(cls.name))
        return blueprint

    def dispatch_request(self):
        return self.table.render()
