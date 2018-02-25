from django.core.management.base import BaseCommand, CommandError
from pytesseract import image_to_string
from PIL import Image
import os

class Command(BaseCommand):
	help = 'converts image to text'

	def handle(self, *args, **options):
            print(os.path.join())
            print(image_to_string(Image,open('o.png')))