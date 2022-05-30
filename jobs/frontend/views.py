from django.shortcuts import render

from jobs.models import Job


def home(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "index.html", context)
