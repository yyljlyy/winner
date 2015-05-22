__author__ = 'lee'
from django.db import models
from django.utils.encoding import smart_unicode

class UserProfile(models.Model):
    """
    """
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=10)
    address = models.CharField(max_length=50)


    class Meta:
        app_label = "winner"

    def __unicode__(self):
        return smart_unicode(u"%s" % self.name)