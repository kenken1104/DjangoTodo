# Generated by Django 2.0 on 2018-09-24 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180924_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]