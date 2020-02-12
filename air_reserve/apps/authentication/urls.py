from django.urls import path
from .views import SignupUser, SignupAdmin, LoginView


urlpatterns = [
    path('auth/signup/', SignupUser.as_view(), name='user_signup'),
    path('auth/admin/signup/', SignupAdmin.as_view(), name='admin_signup'),
    path('auth/login/', LoginView.as_view(), name='user_login')
]
