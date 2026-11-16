import unittest

from rest_api import app


class RestApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_list_services_includes_ids_and_service_data(self):
        response = self.client.get("/services")
        services = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(services)
        self.assertTrue(all("id" in service for service in services))
        self.assertIn("name", services[0])
        self.assertIn("number", services[0])

    def test_get_existing_service(self):
        response = self.client.get("/services/ambulance")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], "ambulance")
        self.assertEqual(response.get_json()["number"], "110")

    def test_unknown_service_returns_not_found(self):
        response = self.client.get("/services/not-a-service")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Service not found"})


if __name__ == "__main__":
    unittest.main()
