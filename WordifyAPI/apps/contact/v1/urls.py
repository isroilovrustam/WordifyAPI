from django.urls import path
from .views import ContactListCreateAPIView

urlpatterns = [
    path('contact-list-create/', ContactListCreateAPIView.as_view()),
]