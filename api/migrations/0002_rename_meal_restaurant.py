# Generated by Django 4.0.3 on 2022-03-26 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meal',
            new_name='Restaurant',
        ),
    ]