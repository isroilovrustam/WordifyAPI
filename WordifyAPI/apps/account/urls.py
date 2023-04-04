from django.urls import path, include

urlpatterns = [
    path('vi/', include('apps.account.v1.urls')),
]