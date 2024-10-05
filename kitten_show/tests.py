from rest_framework.test import (APITestCase,
                                 APIClient)
from rest_framework import status
from kitten_show.models import Kitten
from users.models import CustomUser


class KittensTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(email='user@123.123', password='qwe123')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.kitten = Kitten.objects.create(
            name='test',
            color='test',
            age=10,
            breed='test',
            description='test'
        )

    def test_kitten_create(self):

        data = {
            'name': self.kitten.name,
            'color': self.kitten.color,
            'age': self.kitten.age,
            'breed': self.kitten.breed,
            'description': self.kitten.description
        }

        response = self.client.post(
            '/kitten_show/kitten_create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


