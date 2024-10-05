from rest_framework import generics, status
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя, обязательными полями являются email и password"""
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = request.data['password']
        user = CustomUser.objects.get(pk=serializer.data['id'])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserProfileAPIView(generics.ListAPIView):
    """Вывод профиля пользователя"""
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
