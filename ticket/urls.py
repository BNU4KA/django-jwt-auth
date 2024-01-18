from django.urls import path
from account.views import *


urlpatterns = [
    path(route="create/", view=UserRegistrationView.as_view(), name="register"),
    path(route="login/", view=UserLoginView.as_view(), name="login"),
    path(route="profile/", view=UserProfileView.as_view(), name="profile"),
]


