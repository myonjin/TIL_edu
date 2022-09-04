from django.urls import path
# 경로는 명시적으로 표현하는게 맞다.
from . import views

urlpatterns = [
    # index 페이지
    path('lotto/', views.lotto, name='lotto'),

]
