# Generated by Django 3.1.4 on 2020-12-24 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdhkl_app', '0002_destinations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Destinations',
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bdhkl_app.post',),
        ),
    ]
