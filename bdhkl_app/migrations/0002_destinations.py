# Generated by Django 3.1.4 on 2020-12-23 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdhkl_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bdhkl_app.post')),
            ],
            bases=('bdhkl_app.post',),
        ),
    ]