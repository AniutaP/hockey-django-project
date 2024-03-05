from django.urls import path
from hockey_django_project.skills.views import (SkillsListView, SkillCreateView,
                                                SkillUpdateView, SkillDeleteView,
                                                )


urlpatterns = [
    path('', SkillsListView.as_view(), name='skills_list'),
    path('create/', SkillCreateView.as_view(), name='create_skill'),
    path('<int:pk>/update/', SkillUpdateView.as_view(), name='update_skill'),
    path('<int:pk>/delete/', SkillDeleteView.as_view(), name='delete_skill'),
]
