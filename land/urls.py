from django.urls import path

from land import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy', views.buy, name='buy'),
]
