# Generated by Django 4.0.3 on 2022-03-26 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_delete_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donations',
            name='sufficient_for',
            field=models.CharField(max_length=155),
        ),
    ]
