import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    a_title = models.CharField(max_length=100, default="None")
    a_text = models.CharField(max_length=3000, default="None")
    a_editor = models.CharField(max_length=100, default="None")
    a_author = models.CharField(max_length=100, default="None")
    ROMAN = 1
    SCI_FI = 2
    NOVELS = 3
    BOOK_TYPE = (
        (ROMAN, 'Roman'),
        (SCI_FI, 'Sci-Fi'),
        (NOVELS, 'Nouvelles'),
    )
    a_type = models.PositiveSmallIntegerField(
        choices=BOOK_TYPE,
        default=ROMAN,
    )
    a_reading_time = models.IntegerField(default=5)
    a_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.a_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.a_pub_date <= now

    was_published_recently.admin_order_field = 'a_pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'