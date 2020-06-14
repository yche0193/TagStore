from django.db import models



class Upload_IMG(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    image = models.ImageField(upload_to='images', verbose_name='images', null=True)
    def __unicode__(self):
        return self.name


