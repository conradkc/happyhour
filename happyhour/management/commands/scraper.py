from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from .models import Restaurant
from django.utils import timezone

class Command(BaseCommand):
    help = 'converts image to text'

    def handle(self, *args, **options):
        for x in range(0,30):
            start = str(x*10)
            html = urlopen('https://www.yelp.com/search?find_desc=Happy+Hour&find_loc=Honolulu,+HI&start=' + start)
            webpage = BeautifulSoup(html.read())
            names = webpage.find_all('a', class_='biz-name js-analytics-click')
            addresses = webpage.find_all('div', class_='secondary-attributes')
            for x in range(len(names)):
                restaurant = Restaurant.objects.get_or_create(
                    pub_date = timezone.now(),
                    name = names[x],
                )

