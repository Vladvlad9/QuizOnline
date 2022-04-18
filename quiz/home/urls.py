
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    path('quiz/', views.quiz, name='quiz'),

    path("signup/", views.SignUp.as_view(), name="signup"),
]