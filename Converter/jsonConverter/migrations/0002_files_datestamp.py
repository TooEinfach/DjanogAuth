# Generated by Django 3.1.6 on 2021-02-18 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jsonConverter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='datestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]