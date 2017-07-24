# -*- coding: utf8 -*-
from flask_table.model import Model
from tests import TestBase


class TestTable(TestBase):
    def test_table(self):
        table = self.table
        self.assertTrue(issubclass(table.model, Model))
