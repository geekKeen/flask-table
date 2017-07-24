# -*- coding: utf8 -*-
from .view import TableView
from flask_bootstrap import Bootstrap


class Page(object):
    def __init__(self, app=None):
        self.views = []
        self.app = None
        self.url_prefix = '/page'
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        # 检测是否已使用 flask-bootstrap
        if self.app.config.get("BOOTSTRAP_USE_MINIFIED", None) is None:
            Bootstrap(self.app)

    def add_view(self, view):
        assert issubclass(view, TableView), "view must be TableView subclass"
        self.views.append(view)
        self.app.register_blueprint(view.create_blueprint(self))
