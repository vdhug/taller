import unittest
from .venmo import MiniVenmo, User

class TestUser(unittest.TestCase):

    def test_create_user(self):
        venmo = MiniVenmo()
        vitor_user = venmo.create_user(name="Vitor", balance=200)
        self.assertIsInstance(vitor_user, User)
        self.assertEquals(vitor_user.activities, [])
        self.assertEquals(vitor_user.name, "Vitor")
        self.assertEquals(vitor_user.balance, 200)
    

    def test_pay(self):
        venmo = MiniVenmo()
        vitor_user = venmo.create_user(name="Vitor", balance=200)
        diego_user = venmo.create_user(name="Vitor", balance=200)

        vitor_user.pay(user=diego_user, quantity=5.00, reason="Coffee")
        self.assertEquals(vitor_user.balance, 195)
        self.assertEquals(diego_user.balance, 205)
