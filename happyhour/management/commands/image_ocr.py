from django.core.management.base import BaseCommand, CommandError
from os import listdir
from os.path import isfile, join
from django.conf import settings
from happyhour.models import Restaurant,HappyHour
from dateparser.search import search_dates
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
            if len(file_name) > 10:
                restaurant = Restaurant.objects.filter(name__startswith='{:.7}'.format(file_name))
            else:
                restaurant = Restaurant.objects.filter(name__startswith=file_name.split('.')[0])

            print(file_name)
            if restaurant:
                if file_name[-4:] == '.jpg':
                    image_path = join(path,file_name)

                    description = ImageToStringTimeDuration(image_path)


                    print(search_dates(description, settings= {'TIMEZONE': 'HST'}))
                else:
                    txt_path = join(path, file_name)
                    with open(txt_path, 'r') as file:
                        description = file.read()
                        restaurant.description = description
                        print(search_dates(description, settings={'TIMEZONE': 'HST'}))

                #happyhour = HappyHour.objects.create(description=description)
                #happyhour.save()

            else:
                try:
                    print('No Restaurant model for: ' + file_name)
                except:
                    print('something went wrong')

