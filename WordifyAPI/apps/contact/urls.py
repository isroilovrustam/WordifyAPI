from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.contact.v1.urls')),
]