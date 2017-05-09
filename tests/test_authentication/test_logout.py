# -*- coding: utf-8 -*-
from unittest.mock import patch
from portfolio.core.tests import ExtendedTestCase
from portfolio.user.models import User


class TestLogout(ExtendedTestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='williandmorais@gmail.com', password='mudar123')

    def test_invalid_auth(self):
        response = self.client.delete(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'test123')
        )

        self.assertDictEqual(response.json(), {'error': 'invalid_credential'})
        self.assertEqual(response.status_code, 401)

    @patch.multiple('uuid.UUID', hex='9db5c6bffdbb4be4a77bd3be68c7d9eb')
    @patch('django.core.cache.cache.delete')
    def test_logout(self, cache_mock):
        response = self.client.delete(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.bearer_auth('williandmorais@gmail.com', 'mudar123')
        )

        cache_mock.assert_called_with(b'9db5c6bffdbb4be4a77bd3be68c7d9eb')
        self.assertEqual(response.status_code, 204)
