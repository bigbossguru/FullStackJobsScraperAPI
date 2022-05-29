from django.core.management.base import BaseCommand
from django.db import IntegrityError

from scraper.scraper import scrapers

from jobs.models import Job


class Command(BaseCommand):
    def handle(self, *args, **options):

        for data in scrapers():
            try:
                Job.objects.create(**data)
            except IntegrityError:
                continue

        self.stdout.write(self.style.SUCCESS("Successfully"))
