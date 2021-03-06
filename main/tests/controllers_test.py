from base import AppTestCase

class ControllersTest(AppTestCase):
    
    def setUp(self):
        super(ControllersTest, self).setUp()

    def test_login(self):
        successful_data = {"main_username": "admin", "main_password": "admin"}
        
        success_case = self.client.post("/login/", data=successful_data)
        self.assertEqual(302, success_case.status_code)

        nonexistent_data = {"main_username": "nimda", "main_password": "nimda"}

        fail_case = self.client.post("/login/", data=nonexistent_data)
        # Should just render the login page with flash messages.
        self.assertEqual(200, fail_case.status_code)

    def test_logged_in_redirect(self):
        successful_data = {"main_username": "admin", "main_password": "admin"}
        
        success_case = self.client.post("/login/", data=successful_data)
        self.assertEqual(302, success_case.status_code)

        visit_redirect = self.client.get("/login/")
        self.assertEqual(302, visit_redirect.status_code)
