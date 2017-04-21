# -*- coding: utf-8 -*-
from unittest.mock import patch
from bellacia.core.tests import ExtendedTestCase
from bellacia.user.models import User


class TestCheck(ExtendedTestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='williandmorais@gmail.com', password='mudar123')

    def test_invalid_auth(self):
        response = self.client.get(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'test123')
        )

        self.assertDictEqual(response.json(), {'error': 'invalid_credential'})
        self.assertEqual(response.status_code, 401)

    @patch.multiple('uuid.UUID', hex='9db5c6bffdbb4be4a77bd3be68c7d9eb')
    def test_check(self):
        response = self.client.get(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'mudar123')
        )

        self.assertDictEqual(response.json(), {
            '_links': {'user': '/v1/users/1/'},
            'expires_in': 0,
            'token': '9db5c6bffdbb4be4a77bd3be68c7d9eb'
        })
        self.assertEqual(response.status_code, 200)
