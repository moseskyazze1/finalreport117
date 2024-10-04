from django.urls import path
from .views import projects_list, experience_list

from django.conf.urls.static import static
from django.conf import settings

urlpatterns= [
    path("", projects_list, name="projects_list"),
    path("experience/", experience_list, name="experience_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

