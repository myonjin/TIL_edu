from django.urls import path
# 경로는 명시적으로 표현하는게 맞다.
from . import views

urlpatterns = [
    # index 페이지
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('ping/', views.throw, name='throw'),
    path('pong/', views.catch, name='catch'),
    path('<str:name>/', views.profile, name='profile'),
]
