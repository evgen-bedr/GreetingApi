import unittest
import json
from app import app


class TestGreetingAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_default_greeting(self):
        result = self.app.get("/api/greeting")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["greeting"], "hello")

    def test_post_greeting(self):
        result = self.app.post("/api/greeting", json={"greeting": "Hi there!"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["greeting"], "Hi there!")

    def test_get_updated_greeting(self):
        self.app.post("/api/greeting", json={"greeting": "Hi there!"})
        result = self.app.get("/api/greeting")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["greeting"], "Hi there!")

    def test_post_empty_greeting(self):
        result = self.app.post("/api/greeting", json={"greeting": ""})
        self.assertEqual(result.status_code, 400)
        self.assertIn("error", json.loads(result.data))

    def test_post_long_greeting(self):
        long_greeting = "a" * 101
        result = self.app.post("/api/greeting", json={"greeting": long_greeting})
        self.assertEqual(result.status_code, 400)
        self.assertIn("error", json.loads(result.data))

    def test_post_invalid_json(self):
        result = self.app.post(
            "/api/greeting", data="Invalid JSON", content_type="application/json"
        )
        self.assertEqual(result.status_code, 400)
        self.assertIn("error", json.loads(result.data))

    def test_get_invalid_url(self):
        result = self.app.get("/api/invalid")
        self.assertEqual(result.status_code, 404)
        self.assertIn("error", json.loads(result.data))
