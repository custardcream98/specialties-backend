from django.urls import path
from communities.api.views import CommunityView


urlpatterns = [
    path(r'', CommunityView.as_view()),
    # path(r'<>', CommunityView.as_view()),
]