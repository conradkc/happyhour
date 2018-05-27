from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from happyhour.models import Restaurant
from django.utils import timezone

def strip_hour(dt):
    return dt.replace(hour=0,minute=0,second=0, microsecond=0)

def now():
    return strip_hour(timezone.now())

class Command(BaseCommand):
    help = 'scrapes the web for restaurants'

    def handle(self, *args, **options):
        #get date and strip seconds

        for y in range(0,10):
            start = str(y*10)
            url = 'https://www.yelp.com/search?find_desc=Happy+Hour&find_loc=Honolulu,+HI&start=' + start
            print('url: ' + url )
            html = urlopen(url)
            webpage = BeautifulSoup(html.read(), "lxml")
            names = webpage.find_all('a', class_='biz-name js-analytics-click')
            addresses = webpage.find_all('div', class_='secondary-attributes')
            print(addresses[0].address.string)
            categories = webpage.find_all('div', class_='price-category')

            for x in range(len(names)):
                name = names[x].string
                try:
                    full_address = addresses[x].address.contents
                    address = full_address[0].split('\n')[1].lstrip() + ' ' + full_address[2].split('\n')[0]
                except:
                    try:
                        address = addresses[x].a.contents[0]
                    except:
                        address = 'no address'

                category = categories[x].contents[1].string
                print('This is number ' + str(x))
                print('name: ' + name.replace(u"\u2018", "'").replace(u"\u2019", "'"))
                print('address: ' + address.replace(u"\u2018", "'").replace(u"\u2019", "'"))
                #print('category: ' + category)
                restaurant,got = Restaurant.objects.get_or_create(
                    pub_date = now(),
                    name = name.replace(u"\u2018", "'").replace(u"\u2019", "'"),
                    address = address.replace(u"\u2018", "'").replace(u"\u2019", "'"),
                    category = category,
                )
                if not got:
                    restaurant.save()


