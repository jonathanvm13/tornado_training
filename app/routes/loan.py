from app.routes.handler import HttpHandler
from app.utils import parseJson


class LoanHandler(HttpHandler):
    def register(self, data):
        jsonData = parseJson(data)
        if ('business' in jsonData and 'amount' in jsonData['business']):
            requested_amount = int(jsonData['business']['amount'])
            message = "Undecided"

            if requested_amount > 50000:
                message = "Declined"
            elif requested_amount < 50000:
                message = "Approved"

            self.respond(message)

        else:
            message = "No enviaste la informacion correcta"
            self.respond(message, 400)

LoanRoute = (r"/loan/(?P<action>[a-zA-Z]+)?", LoanHandler)
