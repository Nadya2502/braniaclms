from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from http import HTTPStatus

import authapp
import mainapp
from authapp.models import User
from mainapp.models import News

class StaticPagesSmokeTest(TestCase):

    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

class NewsNestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        for i in range(10):
            News.objects.create(
                title=f'News{i}',
                preamble=f'Preamble{i}',
                body=f'body{i}'
            )
        User.objects.create_superuser(username='django', password='geekbrains')
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')
        self.client_with_auth.post(
            auth_url,
            {'username':'django', 'password':'geekbrains'}
        )

    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_open_add_by_anonym(self):
        url = reverse('mainapp:news_create')

        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_create_news_item_by_admin(self):

        news_count = News.objects.all().count()

        url = reverse('mainapp:news_create')
        result = self.client_with_auth.post(
            url,
            data={
                'title':'Test news',
                'preamble':'Test preamble',
                'body':'Test body'
            }
        )
        self.assertEqual(result.status_code, HTTPStatus.FOUND)
        self.assertEqual(News.objects.all().count(), news_count + 1)

class TestTaskMailSend(TestCase):
    fixtures = ("authapp/fixtures/001_user_admin.json",)
    def test_mail_send(self):
        message_text = "test_message_text"
        user_obj = authapp.models.CustomUser.objects.first()
        mainapp.tasks.send_feedback_mail(
            {"user_id": user_obj.id, "message": message_text}
        )
        self.assertEqual(mail.outbox[0].body, message_text)