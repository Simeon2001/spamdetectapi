from django.db import models

# collect new data to train ML model

class New_data(models.Model):
    CONDITION = (('SPAM', 'SPAM'), ('HAM', 'HAM'),)
    message = models.TextField(max_length=100,blank=False)
    _class = models.CharField(max_length=4,blank=False,choices=CONDITION)

    def __str__(self):
        return self._class


