# -*- coding: utf-8 -*-
from base64 import b64encode
from rest_framework.test import APITransactionTestCase


class ExtendedTestCase(APITransactionTestCase):
    maxDiff = None
    reset_sequences = True

    def basic_auth(self, username, password):
        token = '{}:{}'.format(username, password).encode()
        return 'Basic {}'.format(b64encode(token).decode())

    def bearer_auth(self, username, password):
        response = self.client.post(
            '/v1/auth/',
            HTTP_AUTHORIZATION=self.basic_auth(username, password)
        )

        return 'Bearer {}'.format(response.data.get('token'))
