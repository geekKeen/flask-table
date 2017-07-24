# -*- coding: utf8 -*-
from flask import render_template

from .model import Model


class TableMeta(type):
    def __new__(cls, classname, base, fields):
        cls.model = fields.get("model") or Model
        cls.columns = cls.model.columns.keys()
        cls.column_labels = {column: column for column in cls.columns}
        return super(TableMeta, cls).__new__(cls, classname, base, fields)


class TableBase(object):
    """
    控制 Table 的渲染
    能够自定义内容
    """
    __metaclass__ = TableMeta
    template = "table.html"

    @classmethod
    def render(cls):
        return render_template(cls.template, columns=cls.columns, column_labels=cls.column_labels,
                               rows=cls.model.get_result_set())
