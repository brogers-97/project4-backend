from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Trade, Follower
import json


class MainAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.create_user(
            username="testuser", password="12345", zip_code="85207"
        )
        self.user2 = get_user_model().objects.create_user(
            username="otheruser", password="12345", zip_code="85207"
        )

    def test_register_endpoint(self):
        response = self.client.post(
            "/register/",
            json.dumps({"username": "testuser2", "password": "12345", "zip_code": "85207"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        print(response.content)

    def test_login_endpoint(self):
        response = self.client.post(
            "/login/",
            json.dumps({"username": "testuser", "password": "12345"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_logout_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 200)

    def test_create_trade_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            "/trades/",
            json.dumps(
                {
                    "asset_type": "STOCK",
                    "ticker": "AAPL",
                    "quantity": 10,
                    "price": 100.0,
                    "trade_type": "BUY",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_get_portfolio_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_get_users_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_follow_user_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post("/users/otheruser/follow/")
        self.assertEqual(response.status_code, 201)

    def test_follow_unfollow_user_endpoint(self):
        self.client.login(username="testuser", password="12345")

        # test follow
        response = self.client.post("/users/otheruser/follow/")
        self.assertEqual(response.status_code, 201)

        # test unfollow
        response = self.client.delete("/users/otheruser/unfollow/")
        self.assertEqual(response.status_code, 200)

    def test_get_user_portfolio_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/users/testuser/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_get_user_trades_endpoint(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get("/users/testuser/trades/")
        self.assertEqual(response.status_code, 200)

    def test_search_asset_endpoint(self):
        response = self.client.get("/assets/search/AAPL/")
        self.assertEqual(response.status_code, 200)

    def test_get_asset_prices_endpoint(self):
        response = self.client.get("/assets/prices/AAPL/")
        self.assertEqual(response.status_code, 200)
