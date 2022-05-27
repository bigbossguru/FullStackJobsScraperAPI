from django.urls import path, include

from .views import JobsListView

urlpatterns = [
    path("", include("frontend.urls")),
    path("api/v1/jobs/", JobsListView.as_view(), name="jobs"),
]
