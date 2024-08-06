from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

class ArticleList(models.Model):
    url = models.CharField(max_length=1024, blank=True, default='')
    processed = models.BooleanField()

    class Meta:
        db_table = 'article_list'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    date_published = models.DateTimeField()
    description = models.TextField()
    headline = models.CharField(max_length=1024, blank=True, default='')
    url = models.CharField(max_length=1024, blank=True, default='')
    main_image = models.CharField(max_length=1024, blank=True, default='')
    tags = models.CharField(max_length=1024, blank=True, default='')

    class Meta:
        db_table = 'articles'
        ordering = ['id']


class Band(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, blank=True, default='')
    website_url = models.CharField(max_length=1024, blank=True, default='')
    image_url = models.CharField(max_length=1024, blank=True, default='')
    seatgeek_slug = models.CharField(max_length=1024, blank=True, default='')

    class Meta:
        db_table = 'bands'
        ordering = ['name']


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    band_id = models.IntegerField()
    name = models.CharField(max_length=1024, blank=True, default='')
    event_id = models.CharField(max_length=1024, blank=True, default='')
    url = models.CharField(max_length=1024, blank=True, default='')
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=1024, blank=True, default='')
    city = models.CharField(max_length=1024, blank=True, default='')
    state = models.CharField(max_length=1024, blank=True, default='')
    country = models.CharField(max_length=1024, blank=True, default='')
    image_url = models.CharField(max_length=1024, blank=True, default='')

    class Meta:
        db_table = 'shows'
        ordering = ['id']


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, default='')
    email = models.CharField(max_length=1024, blank=True, default='')
    message = models.CharField(max_length=2000, blank=True, default='')
    date_received = models.DateField(auto_now_add=True)
    send_copy = models.BooleanField()
    answered = models.BooleanField()
    reference = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        db_table = 'contact'
        ordering = ['id']


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, default='')
    email = models.CharField(max_length=1024, blank=True, default='')
    date_subscribed = models.DateTimeField(auto_now_add=True)
    date_unsubscribed = models.DateTimeField(null=True)
    date_last_sent = models.DateTimeField(null=True)

    class Meta:
        db_table = 'newsletter'


class Userbands(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    band_id = models.IntegerField()
    band_name = models.CharField(max_length=1024, blank=True, default='')
    band_selected = models.BooleanField()

    class Meta:
        db_table = 'userbands'
        ordering = ['user_id', 'band_id']


@receiver(user_signed_up)
def update_userbands_on_signup(sender=User, **kwargs):
    print('user_signed_up signal received')
    user = kwargs['user']
    bands = Band.objects.all()
    for band in bands:
        userband = Userbands(user_id=user.id,
                             band_id=band.id,
                            band_name=band.name,
                            band_selected=True)
        userband.save()
    print('userbands updated')

@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    user_email = instance.email
    username = user_email
    instance.username = username
    print("update_username_from_email")