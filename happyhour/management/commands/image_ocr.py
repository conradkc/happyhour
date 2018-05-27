from django.core.management.base import BaseCommand, CommandError
from os import listdir
from os.path import isfile, join
from django.conf import settings
from happyhour.models import Restaurant,HappyHour
import argparse
import io
from happyhour.ocr import ConvertToStartDuration, ImageToStringTimeDuration


class Command(BaseCommand):
    help = 'Takes images in /happyhour/media and creates happy hours and links them to respective Restaurants'


    def handle(self, *args, **options):
        root_path = settings.BASE_DIR
        path = join(root_path, 'happyhour', 'media')
        file_names = [f for f in listdir(path) if isfile(join(path, f))]
        for file_name in file_names:
            restaurant = Restaurant.objects.filter(name__startswith='{:.7}'.format(file_name))
            if restaurant:
                image_path = join(path,file_name)
                ImageToStringTimeDuration(image_path)
            else:
                try:
                    print('No Resteraunt model for: ' + file_name)
                except:
                    print('something went wrong')

