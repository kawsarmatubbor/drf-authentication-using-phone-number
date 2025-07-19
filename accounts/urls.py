from django.urls import path
from .views import RegistrationView, LoginView, logout_view

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view)
]
