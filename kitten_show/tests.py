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
            description='test',
            owner=self.user
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

        self.assertEqual(
            response.json(),
            {'id': 3, 'name': 'test', 'color': 'test', 'age': 10,
             'breed': 'test', 'description': 'test'}
        )

    def test_breeds(self):
        response = self.client.get(
            '/kitten_show/breeds/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'name': 'test', 'breed': 'test'}]
        )

    def test_kittens(self):
        response = self.client.get(
            '/kitten_show/kittens/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 7, 'name': 'test', 'color': 'test', 'age': 10,
              'breed': 'test', 'description': 'test'}]
        )

    def test_kitten_view(self):
        response = self.client.get(
            f'/kitten_show/kitten_view/{self.kitten.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'name': 'test', 'color': 'test', 'age': 10,
             'breed': 'test', 'description': 'test'}
        )

    def test_kitten_update(self):
        data = {
            'name': 'qwe',
        }

        response = self.client.patch(
            f'/kitten_show/kitten_update/{self.kitten.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 5, 'name': 'qwe', 'color': 'test', 'age': 10,
             'breed': 'test', 'description': 'test'}
        )

    def test_kitten_delete(self):
        response = self.client.delete(
            f'/kitten_show/kitten_delete/{self.kitten.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
