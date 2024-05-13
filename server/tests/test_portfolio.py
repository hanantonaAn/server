import unittest
import requests
from django.urls import reverse
from user.models import *


class SphereTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_create_sphere(self):
        Sphere.objects.filter(sphere='Frontend developing').delete()
        url = 'http://localhost:8000' + reverse('sphere-list')

        data = {'sphere': 'Frontend developing'}

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(Sphere.objects.count(), 1)

        sphere = Sphere.objects.get()
        self.assertEqual(sphere.sphere, 'Frontend developing')

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_auth_user(self):
        url = 'http://127.0.0.1:8000/auth/jwt/create/'

        data = {
                    "username": "hello6@mail.ru",
                    "password": "defe1234"
                }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)    

class AuthWithWrongEmailTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_auth_user(self):
        url = 'http://127.0.0.1:8000/auth/jwt/create/'

        data = {
                    "username": "hello6_fail@mail.ru",
                    "password": "defe1234"
                }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 401)      
        self.assertEqual(response.json(), 
        {
            "detail": "No active account found with the given credentials"
        })        

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_create_user(self):
        email = "hello_1002"
        name = "hello_1002"
        User.objects.filter(username=name).delete()
        url = 'http://127.0.0.1:8000/auth/users/' 

        data = {
                    "email": email,
                    "username": name,
                    "password": "defe1234",
                    "re_password": "defe1234"
                }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(User.objects.filter(username=name).count(), 1)

        user = User.objects.filter(username=name).get()
        self.assertEqual(user.email, email)   

class PortfolioTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_create_portfolio(self):
        name = "hello_test"
        id = "e4941c42-9b77-4a7a-aaef-874a4329821c"
        Portfolio.objects.filter(user_id=id).delete()
        url = 'http://127.0.0.1:8000/portfolio/' 

        data = {
                    "user_id": "e4941c42-9b77-4a7a-aaef-874a4329821c",
                    "portfolio_html": "string",
                    "portfolio_text": "string",
                    "public": True
                }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 500)

        self.assertEqual(Portfolio.objects.filter(user_id=id).count(), 0)  

                
class FetchVacanciesTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_fetch_vacancies(self):
        name = "hello_test"
        UserVacancy.objects.filter(username=name).delete()
        url = 'http://localhost:8000/fetch_vacancies/?username=hello_test'    

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {"message": "Вакансии успешно получены и сохранены."})  

class VacanciesTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_check_vacancies(self):
        name = "hello_test"
        url = 'http://127.0.0.1:8000/vacancy/?username=hello_test'    

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)       

class CheckUserInfoTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_check_user(self):
        name = "hello_test"
        url = 'http://127.0.0.1:8000/userinfo_username/hello_test/'    

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {
                                                "user": {
                                                    "id": "e4941c42-9b77-4a7a-aaef-874a4329821c",
                                                    "username": "hello_test",
                                                    "email": "hello_test@mail.ru"
                                                },
                                                "user_data": None,
                                                "user_skills": None,
                                                "user_experience": None,
                                                "user_portfolio": None
                                            })                  

class CheckGetUserTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_checing_getuser(self):
        url = 'http://127.0.0.1:8000/users_by_username/hello_test/'    

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), [
                                                {
                                                    "id": "e4941c42-9b77-4a7a-aaef-874a4329821c",
                                                    "username": "hello_test",
                                                    "email": "hello_test@mail.ru"
                                                }
                                            ])                  

class CheckVacancyFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()

    def test_vacancies(self):
        url = 'http://127.0.0.1:8000/vacancies/delete_all_by_username/hello_test/'    

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {
                                                "message": "All vacancies for user hello_test have been deleted."
                                            })     

if __name__ == '__main__':
    unittest.main()
