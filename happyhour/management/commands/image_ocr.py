from django.core.management.base import BaseCommand, CommandError
import argparse
import io

from google.cloud import vision
from google.cloud.vision import types

class Command(BaseCommand):
    help = 'converts image to text'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        pass
