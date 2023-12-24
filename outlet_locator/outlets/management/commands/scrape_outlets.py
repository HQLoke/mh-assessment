from unittest.mock import Base
from django.core.management.base import BaseCommand, CommandError, CommandParser

from . import web_scraper
from . import geocoder

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('states', nargs='*', type=str, help='Choosing state (optional)')
    
    def handle(self, *args, **options):
        states = options['states']
        web_scraper.scrape_website_data(states)
        geocoder.get_geographical_coordinates()
        