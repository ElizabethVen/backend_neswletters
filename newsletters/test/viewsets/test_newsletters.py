from rest_framework.test import APITestCase
from newsletters.models import Newsletter


class NewsletterApiTestCase(APITestCase):


    def setUp(self):
        self.newsletter = Newsletter.objects.create(name='Nuevo', description='Description', target=10)

    def test_retrieve_newsletter(self):
        """
        Crear un retrieve de newsletters
        """
        result = self.client.get('/api/v1/newsletters/{0}/'.format(self.newsletter.id))

        assert result.status_code == 200
        assert result.data['name'] == self.newsletter.name

    def test_list_newsletters(self):
        """
        Lista los newsletters
        """

        result = self.client.get('/api/v1/newsletters/')

        assert result.status_code == 200
        assert result.data['count'] == 1