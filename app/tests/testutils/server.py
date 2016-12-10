"""
Correr el servidor para las pruebas
"""
import json, logging

from tornado.web import Application
from tornado.testing import AsyncHTTPTestCase


class ServerTest(AsyncHTTPTestCase):
    def get_app(self):
        return Application(self.routes, debug=False)

    def post(self, route, data):
        result = self.fetch("/%s" % route,
                            method="POST",
                            body=json.dumps(data)).body

        try:
            return json.loads(result)
        except ValueError:
            raise ValueError(result)
