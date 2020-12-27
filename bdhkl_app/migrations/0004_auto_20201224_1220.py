# Generated by Django 3.1.4 on 2020-12-24 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bdhkl_app', '0003_auto_20201224_1142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Destinations',
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(upload_to='post/')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
