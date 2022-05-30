from django.urls import path, include

from .views import JobsListView

app_name = "api_app"

urlpatterns = [
    path("", include("jobs.frontend.urls")),
    path("api/v1/jobs/", JobsListView.as_view(), name="jobs"),
]
