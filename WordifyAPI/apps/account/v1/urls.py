from rest_framework.authtoken import views
from django.urls import path
from .views import MyProfile

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my/profile/', MyProfile.as_view()),
]