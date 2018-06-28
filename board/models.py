from django.db import models
import time

date_created = time.strftime("%Y/%m/%d")


class AddBoard(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=4000)
    author = models.CharField(max_length=50)
    date = models.CharField(max_length=20, default=date_created)

    def __str__(self):
        return self.title + '-' + self.text + '-' + self.author + '-' + self.date
