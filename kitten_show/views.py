from kitten_show.models import Kitten
from rest_framework import generics
from kitten_show.serializers import KittenSerializer, BreedsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class BreedAPIView(generics.ListAPIView):
    """Вывод пород зарегистрированных кошек"""

    serializer_class = BreedsSerializer
    queryset = Kitten.objects.all().distinct('breed')
    permission_classes = [IsAuthenticated]


class KittenListAPIView(generics.ListAPIView):
    """Вывод всех зарегистрированных кошек,
     принимает get-параметр 'breed' для фильтрации по породам"""

    serializer_class = KittenSerializer
    queryset = Kitten.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed']


class KittenCreateAPIView(generics.CreateAPIView):
    """Регистрация кошки, принимает параметры: name, color, age, breed, description.
     Все параметры являются обязательными. Владелец кошки присваивается ей автоматически"""

    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_kitten = serializer.save()
        new_kitten.owner = self.request.user
        new_kitten.save()


class KittenRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод информации по определенной кошке"""

    serializer_class = KittenSerializer
    queryset = Kitten.objects.all()
    permission_classes = [IsAuthenticated]


class KittenUpdateAPIView(generics.UpdateAPIView):
    """Изменение информации по определенной кошке"""

    serializer_class = KittenSerializer
    queryset = Kitten.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class KittenDeleteAPIView(generics.DestroyAPIView):
    """Удаление кошки из базы данных"""

    serializer_class = KittenSerializer
    queryset = Kitten.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
