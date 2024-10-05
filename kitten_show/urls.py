from django.urls import path
from kitten_show.apps import KittenShowConfig
from kitten_show.views import (BreedAPIView, KittenListAPIView, KittenDeleteAPIView,
                               KittenUpdateAPIView, KittenRetrieveAPIView, KittenCreateAPIView)


app_name = KittenShowConfig.name

urlpatterns = [
    path('breeds/', BreedAPIView.as_view(), name='kitten_breeds'),
    path('kittens/', KittenListAPIView.as_view(), name='kittens'),
    path('kitten_create/', KittenCreateAPIView.as_view(), name='kitten_create'),
    path('kitten_view/<int:pk>/', KittenRetrieveAPIView.as_view(), name='kitten_view'),
    path('kitten_update/<int:pk>/', KittenUpdateAPIView.as_view(), name='kitten_update'),
    path('kitten_delete/<int:pk>/', KittenDeleteAPIView.as_view(), name='kitten_delete')
]
