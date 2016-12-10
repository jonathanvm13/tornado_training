"""
Pruebas para las rutas de Loan
"""
import unittest

from app.tests.testutils.server import ServerTest
from app.routes.loan import LoanRoute


class LoanRouteTest(ServerTest):
    routes = [LoanRoute]

    def test_register_declined(self):
        loan_register = {
            "business": {
                "taxId": "12657",
                "businessName": "LendingFront",
                "businessAddress": "Calle 8",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "555-44",
                "amount": 50001
            },
            "owner": {
                "socialSecurity": "socialSecurity",
                "name": "Jonathan",
                "email": "jonathanvm13@gmail.com",
                "address": "Calle 53A",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "5554-544"
            }
        }

        result = self.post("loan/register", loan_register)

        self.assertIn("status", result)
        self.assertIn("data", result)

        self.assertEqual(
            result["data"],
            "Declined"
        )
        self.assertEqual(
            result["status"],
            200
        )

    def test_register_undecided(self):
        loan_register = {
            "business": {
                "taxId": "12657",
                "businessName": "LendingFront",
                "businessAddress": "Calle 8",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "555-44",
                "amount": 50000
            },
            "owner": {
                "socialSecurity": "socialSecurity",
                "name": "Jonathan",
                "email": "jonathanvm13@gmail.com",
                "address": "Calle 53A",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "5554-544"
            }
        }

        result = self.post("loan/register", loan_register)

        self.assertIn("status", result)
        self.assertIn("data", result)

        self.assertEqual(
            result["data"],
            "Undecided"
        )
        self.assertEqual(
            result["status"],
            200
        )

    def test_register_approved(self):
        loan_register = {
            "business": {
                "taxId": "12657",
                "businessName": "LendingFront",
                "businessAddress": "Calle 8",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "555-44",
                "amount": 49999
            },
            "owner": {
                "socialSecurity": "socialSecurity",
                "name": "Jonathan",
                "email": "jonathanvm13@gmail.com",
                "address": "Calle 53A",
                "city": "Medellin",
                "state": "Antioquia",
                "postalCode": "5554-544"
            }
        }

        result = self.post("loan/register", loan_register)

        self.assertIn("status", result)
        self.assertIn("data", result)

        self.assertEqual(
            result["data"],
            "Approved"
        )
        self.assertEqual(
            result["status"],
            200
        )

    def test_register_error(self):
        loan_register = {}

        result = self.post("loan/register", loan_register)

        self.assertIn("status", result)
        self.assertIn("data", result)

        self.assertEqual(
            result["data"],
            "No enviaste la informacion correcta"
        )
        self.assertEqual(
            result["status"],
            400
        )


if __name__ == "__main__":
    unittest.main()
