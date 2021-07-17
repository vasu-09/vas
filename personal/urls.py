from django.urls import path
from . import views

urlpatterns=[
	path('/', views.home, name="home"),
	path('quiz/', views.home2, name="quiz")
]