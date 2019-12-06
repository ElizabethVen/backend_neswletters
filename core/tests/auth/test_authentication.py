# importo el usuario
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationTestCase(APITestCase):
    """
    encapsula las reglas de autenticación
    """

    def setUp(self):
        """
        crea un usaurio que se guarda en la variable user
        """
        self.user = User.objects.create_user('test_user', 'test_user@gmail.com', '123456')

    def test_authenticate(self):
        """
        manda un post y tiene que regresa un token
        """
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})

        assert result.status_code == 200
        assert 'access' in result.data

    def test_valid_token(self):
        """
        valida el token
        """
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']

        users_result = self.client.get('/api/v1/users/', HTTP_AUTHORIZATION = 'BEARER {0}'.format(token))

        assert users_result.status_code == 200