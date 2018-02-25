from django.db import models

class Restaurant(models.Model):
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length = 200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(max_length = 200)

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
        max_length = 2,
        choices = DAYS_OF_THE_WEEK_CHOICES,
    )
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
    )
    has_food = models.BooleanField(default=False)
    has_drink = models.BooleanField(default=False)
    Image = models.ImageField()