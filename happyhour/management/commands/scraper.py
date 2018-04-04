from django.core.management.base import BaseCommand, CommandError
import argparse
import io
from bs4 import BeautifulSoup
import urllib3

class Command(BaseCommand):
    help = 'converts image to text'

    def handle(self, *args, **options):
        url = 'https://www.yelp.com/search?find_desc=Happy+Hour&find_loc=Honolulu,+HI&start=0'
        http = urllib3.PoolManager()
        page = http.request('GET', url)
        soup = BeautifulSoup(page, "html.parser")
        place_name = soup.find_all('span')
        print(place_name)