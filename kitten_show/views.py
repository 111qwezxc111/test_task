from kitten_show.models import Kitten, Grade
from rest_framework import generics, mixins
from kitten_show.serializers import KittenSerializer, BreedsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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


class KittenRetrieveAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """Вывод информации по определенной кошке при get запросе. При post запросе добавление оценки.
     Для того, чтобы оценить котенка добавьте ключ 'grade' в тело запроса и укажите оценку цифрой"""

    serializer_class = KittenSerializer
    queryset = Kitten.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        grade_value = self.request.data.get('grade')

        if isinstance(grade_value, int) and grade_value > 0:
            kitten = get_object_or_404(Kitten, pk=kwargs.get('pk'))
            grade = Grade.objects.get_or_create(user=self.request.user, kitten=kitten, value=grade_value)
            return HttpResponse('Оценка добавлена' if grade[-1] else 'Оценка была добавлена ранее')

        return HttpResponse('Оценка указана некорретно либо не указана вовсе')


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
