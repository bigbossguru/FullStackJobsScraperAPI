from rest_framework import generics, permissions

from .models import Job
from .serializers import JobSerializer


class JobsListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
