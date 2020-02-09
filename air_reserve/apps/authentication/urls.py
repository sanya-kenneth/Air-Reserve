from django.urls import path
from .views import SignupUser, SignupAdmin


urlpatterns = [
    path('users/', SignupUser.as_view()),
    path('users/admin/', SignupAdmin.as_view())
]
