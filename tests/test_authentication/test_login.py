# -*- coding: utf-8 -*-
from unittest.mock import patch
from portfolio.core.tests import ExtendedTestCase
from portfolio.user.models import User


class TestLogin(ExtendedTestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='williandmorais@gmail.com', password='mudar123')

    @patch.multiple('uuid.UUID', hex='9db5c6bffdbb4be4a77bd3be68c7d9eb')
    def test_login(self):
        response = self.client.post(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.basic_auth('williandmorais@gmail.com', 'mudar123')
        )

        self.assertDictEqual(response.json(), {
            '_links': {'user': '/v1/users/1/'},
            'expires_in': 3600,
            'token': '9db5c6bffdbb4be4a77bd3be68c7d9eb'
        })
        self.assertEqual(response.status_code, 201)

    @patch.multiple('uuid.UUID', hex='9db5c6bffdbb4be4a77bd3be68c7d9eb')
    def test_login_refresh(self):
        response = self.client.post(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'mudar123'),
            format='json'
        )

        self.assertDictEqual(response.json(), {
            '_links': {'user': '/v1/users/1/'},
            'expires_in': 3600,
            'token': '9db5c6bffdbb4be4a77bd3be68c7d9eb'
        })
        self.assertEqual(response.status_code, 201)

    @patch.multiple('uuid.UUID', hex='9db5c6bffdbb4be4a77bd3be68c7d9eb')
    def test_login_invalid_credentials(self):
        response = self.client.post(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'taerrado'),
            format='json'
        )

        self.assertDictEqual(response.json(), {'error': 'invalid_credential'})
        self.assertEqual(response.status_code, 401)
