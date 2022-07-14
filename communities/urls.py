from django.urls import path
from communities.api.views import CommunityView, CertainCommunityView


urlpatterns = [
    path(r'', CommunityView.as_view()),
    path(r'<str:community_id>/', CertainCommunityView.as_view()),
]