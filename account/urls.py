from django.urls import path
from account.views import *


urlpatterns = [
    path(route="register/", view=UserRegistrationView.as_view(), name="register"),
    path(route="login/", view=UserLoginView.as_view(), name="login"),
    path(route="profile/", view=UserProfileView.as_view(), name="profile"),
    path(route="profiles/", view=UserProfilesView.as_view(), name="profiles"),
    path(route="update/", view=UpdateUserProfileView.as_view(), name="update"),
    path(route="changePassword/", view=UserChangePasswordView.as_view(), name="changePassword"),
    path(route="sendResetPasswordEmail/", view=SendResetPasswordEmailView.as_view(), name="sendResetPasswordEmail"),
    path(route="resetPassword/<userId>/<token>/", view=UserResetPasswordView.as_view(), name="resetPassword"),
]


