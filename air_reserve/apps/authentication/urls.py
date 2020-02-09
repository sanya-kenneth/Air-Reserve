from django.urls import path
from .views import SignupUser, SignupAdmin, LoginView


urlpatterns = [
    path('auth/signup/', SignupUser.as_view()),
    path('auth/admin/signup/', SignupAdmin.as_view()),
    path('auth/login/', LoginView.as_view())
]
