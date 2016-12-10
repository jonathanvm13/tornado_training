import tornado.ioloop
import tornado.web

import app.config as CONFIG
from app.routes.loan import LoanRoute


def main(debug=True, port=CONFIG.PORT):
    application = tornado.web.Application([
        LoanRoute
    ], debug=debug
        , autoreload=debug)

    application.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
