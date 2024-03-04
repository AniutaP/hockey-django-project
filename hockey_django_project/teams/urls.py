from django.urls import path
from hockey_django_project.teams.views import (TeamsListView, TeamCreateView,
                                               TeamUpdateView, TeamDeleteView,
                                               )


urlpatterns = [
    path('', TeamsListView.as_view(), name='teams_list'),
    path('create/', TeamCreateView.as_view(), name='create_team'),
    path('<int:pk>/update/', TeamUpdateView.as_view(), name='update_team'),
    path('<int:pk>/delete/', TeamDeleteView.as_view(), name='delete_team'),
]
