from django.db import models
from django.utils.timezone import datetime
from  django.contrib.auth.models import User
# Create your models here.
class Services(models.Model):

    author  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title   = models.CharField(max_length=100)
    content = models.TextField()
    title_box   = models.CharField(max_length=100)
    content_box = models.TextField()
    created = models.DateTimeField(default=datetime.now, blank=True)
    post_slug = models.SlugField(blank=True, null=True)
    image =models.ImageField(upload_to='post/',blank=True, null=True)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.post_slug = self.title
        super(Services,self).save(*args, **kwargs)


    def __str__(self):

        return self.title
