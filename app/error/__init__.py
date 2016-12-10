''''
Excepciones
'''


class AppError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super(Exception, self).__init__(message)


# 400
class InvalidJSON(AppError):
    def __init__(self):
        AppError.__init__(self,
                          "Invalid Json",
                          400
                          )


# 404
class RouteNotFound(AppError):
    def __init__(self, action):
        AppError.__init__(self,
                          "Route Not Found",
                          404
                          )


# 500
class ServerError(AppError):
    def __init__(self):
        AppError.__init__(self,
                          "Internal Server Error",
                          500
                          )
