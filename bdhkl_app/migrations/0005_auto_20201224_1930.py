# Generated by Django 3.1.4 on 2020-12-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdhkl_app', '0004_auto_20201224_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_posted']},
        ),
    ]
