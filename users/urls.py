from django.urls import path
from users.api.views import UserProfileView, CheckUserView, SignUpView, ValidateToken
from core.crypto.validation import VarifySignedMsgView

urlpatterns = [
    path(r'', UserProfileView.as_view()),
    path(r'checkuser/', CheckUserView.as_view()),
    path(r'signup/', SignUpView.as_view()),
    path(r'auth/', VarifySignedMsgView.as_view()),
    path(r'checkpermission/', ValidateToken.as_view())
]