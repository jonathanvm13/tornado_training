import json, traceback
import tornado.web

from tornado_cors import CorsMixin

from app.error import AppError, RouteNotFound, ServerError
from app.utils import LOGGER


class HttpHandler(CorsMixin, tornado.web.RequestHandler):
    # Tornado cors Options
    CORS_ORIGIN = '*'
    CORS_METHODS = 'OPTIONS'
    CORS_HEADERS = 'Content-Type'

    @tornado.web.asynchronous
    def post(self, action):
        print("POST!!!")
        try:
            # Buscar la ruta
            if not hasattr(self, str(action)):
                raise RouteNotFound(action)

            # Enviar la data al metodo encontrado
            handler = getattr(self, str(action))
            handler(self.request.body)
        except AppError as e:
            self.respond(e.message, e.code)
        except Exception as e:
            LOGGER.error(
                "\n\n Server Error\n%s\n%s\n",
                __file__,
                traceback.format_exc()
            )
            error = ServerError()
            self.respond(error.message, error.code)

    def respond(self, data, code=200):
        self.set_status(code)
        self.write({
            "status": code,
            "data": data
        })
        self.finish()
