# Generated by Django 4.2.7 on 2023-12-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam_site', '0005_alter_newsletter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='date_last_sent',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='date_unsubscribed',
            field=models.DateTimeField(null=True),
        ),
    ]