from django.db import models

# Create your models here.

class Topic(models.Model):
    """ A topic user is learning about"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        """ string presentation of topic"""
        return self.title


class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        verbose_name_plural = 'Entries'

    def __str__(self):

        return f"self.text[:50]..."


    

