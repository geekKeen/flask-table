# -*- coding: utf8 -*-
from tests import TestBase


class ViewTest(TestBase):
    def test_view(self):
        with self.app.test_client() as client:
            response = client.get("/page/user_view/")
            self.assertNotEqual(response.status_code, 404)
