from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    pub_date = models.DateTimeField('date published', default= timezone.now)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 400)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default = 0)
    long = models.DecimalField(max_digits=9, decimal_places=6, default = 0)
    category = models.CharField(max_length = 200, null= True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pub_date',)

   # def save(self, *args, **kwargs):


class HappyHour(models.Model):
    MONDAY = 'M'
    TUESDAY = 'T'
    WEDNESDAY = 'W'
    THURSDAY = 'R'
    FRIDAY = 'F'
    SATURDAY = 'S'
    SUNDAY = 'U'
    DAYS_OF_THE_WEEK_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),

    )
    start = models.TimeField()
    duration = models.DurationField(default=0)
    day = models.CharField(
        max_length = 1,
        choices = DAYS_OF_THE_WEEK_CHOICES,
    )
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
    )

    has_food = models.BooleanField(default=False)
    has_drink = models.BooleanField(default=False)
    description = models.TextField(null= True)
    Image = models.ImageField(null= True, upload_to= 'uploads/')