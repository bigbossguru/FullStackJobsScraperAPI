from django.core.management.base import BaseCommand

from jobs.scraper.scraper import web_scraper


class Command(BaseCommand):
    def handle(self, *args, **options):
        web_scraper()
        self.stdout.write(self.style.SUCCESS("Successfully"))
