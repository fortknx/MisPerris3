from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListMascota.as_view()),
    path('<int:pk>/', views.DetalleMascota.as_view()),
]
