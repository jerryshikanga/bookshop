from django.test import TestCase
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
import requests


# Create your tests here.
class PermissionTest(TestCase):
    def __init__(self, *args, **kwargs):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        # self.base_url = "http://localhost:8000/"
        self.base_url = "http://shikanga.pythonanywhere.com/"
        self.login_path = self.base_url + "accounts/login/"
        self.user_register_path = self.base_url + "accounts/register/"
        super(PermissionTest, self).__init__(*args, **kwargs)

    def setUp(self):
        User.objects.create_user(username="jerry", email="jerryshikanga@gmail.com", password="password")
        self.test_sign_in()

    def test_sign_in(self):
        res = self.session.get(self.login_path, headers=self.headers)
        cookies = dict(res.cookies)
        self.assertIsNotNone(cookies)
        soup = BeautifulSoup(res.text, "html.parser")
        element = soup.find("form")
        self.assertIsNotNone(element)
        # < input type = "hidden" name = "csrfmiddlewaretoken" value = "b5zVaFXOG8f5dQRlrNyA19S8H4neQfyTSPCCF6egUnBeKs6OzdEnDPu6EH78yqOw" >
        # csrf_token = soup.find('input', {'name':'csrfmiddlewaretoken'})['value']
        csrf_token = cookies.get('csrftoken', None)
        self.assertIsNotNone(csrf_token)
        payload = dict(username="jerry", password="password", csrfmiddlewaretoken=csrf_token)
        response = self.session.post(self.login_path, data=payload, cookies=cookies, headers=self.headers)
        self.assertLessEqual(int(response.status_code), 300)

    def test_sign_up(self):
        page = self.session.get(self.user_register_path, headers=self.headers)
        cookies = dict(page.cookies)
        self.assertIsNotNone(cookies, msg="No cookies found")
        self.assertIsNotNone(page, msg="Page not found")
        payload = {
            "email": "shikanga@test.mail",
            "password1": "password",
            "password2": "password",
            "first_name": "BeatifulSoup",
            "last_name": "Bot",
            "telephone": "+254789123456",
            "address": "00100 Kenya",
            "csrfmiddlewaretoken": cookies.get("csrftoken"),
            # "group": "1",
        }
        response = self.session.post(self.user_register_path, headers=self.headers, data=payload, cookies=cookies)
        self.assertLess(response.status_code, 400,
                        msg="Http response failed")  # check that status code is <400 i.r. success HTTP Status codes
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.prettify())
        errors = soup.find_all("ul", {"class": "errorlist"})
        if 0 < len(errors):
            [print(error) for error in errors]
        else:
            user = User.objects.get(email="shikanga@test.mail")
            self.assertIsNotNone(user, msg="No user found")
