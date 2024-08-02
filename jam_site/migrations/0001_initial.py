# Generated by Django 4.2.3 on 2024-08-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_published', models.DateTimeField()),
                ('description', models.TextField()),
                ('headline', models.CharField(blank=True, default='', max_length=1024)),
                ('url', models.CharField(blank=True, default='', max_length=1024)),
                ('main_image', models.CharField(blank=True, default='', max_length=1024)),
                ('tags', models.CharField(blank=True, default='', max_length=1024)),
            ],
            options={
                'db_table': 'articles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ArticleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=1024)),
                ('processed', models.BooleanField()),
            ],
            options={
                'db_table': 'article_list',
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('website_url', models.CharField(blank=True, default='', max_length=1024)),
                ('image_url', models.CharField(blank=True, default='', max_length=1024)),
                ('seatgeek_slug', models.CharField(blank=True, default='', max_length=1024)),
            ],
            options={
                'db_table': 'bands',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('email', models.CharField(blank=True, default='', max_length=1024)),
                ('message', models.CharField(blank=True, default='', max_length=2000)),
                ('date_received', models.DateField(auto_now_add=True)),
                ('send_copy', models.BooleanField()),
                ('answered', models.BooleanField()),
                ('reference', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'db_table': 'contact',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('email', models.CharField(blank=True, default='', max_length=1024)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
                ('date_unsubscribed', models.DateTimeField(null=True)),
                ('date_last_sent', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'newsletter',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('band_id', models.IntegerField()),
                ('name', models.CharField(blank=True, default='', max_length=1024)),
                ('event_id', models.CharField(blank=True, default='', max_length=1024)),
                ('url', models.CharField(blank=True, default='', max_length=1024)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('venue', models.CharField(blank=True, default='', max_length=1024)),
                ('city', models.CharField(blank=True, default='', max_length=1024)),
                ('state', models.CharField(blank=True, default='', max_length=1024)),
                ('country', models.CharField(blank=True, default='', max_length=1024)),
                ('image_url', models.CharField(blank=True, default='', max_length=1024)),
            ],
            options={
                'db_table': 'shows',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Userbands',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('band_id', models.IntegerField()),
                ('band_name', models.CharField(blank=True, default='', max_length=1024)),
                ('band_selected', models.BooleanField()),
            ],
            options={
                'db_table': 'userbands',
                'ordering': ['user_id', 'band_id'],
            },
        ),
    ]