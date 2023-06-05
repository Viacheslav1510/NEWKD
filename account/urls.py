from django.urls import path
from .views import (
        index,
        RegistrationView,
        LoginView,
        logout_page
)


app_name = 'account'

urlpatterns = [
    path('', index, name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('signin/', LoginView.as_view(), name='signin'),
]
