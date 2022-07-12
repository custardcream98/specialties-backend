from django.urls import path
from users.api.views import CheckUserView, SignUpView
from core.crypto.validation import VarifySignedMsgView

urlpatterns = [
    #path(r'login/', LoginView.as_view(), name='knox_login'),
    #path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path(r'', CheckUserView.as_view()),
    path(r'signup/', SignUpView.as_view()),
    path(r'auth/', VarifySignedMsgView.as_view()),
]