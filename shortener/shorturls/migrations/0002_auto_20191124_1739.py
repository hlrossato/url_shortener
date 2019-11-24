# Generated by Django 2.2.7 on 2019-11-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shorturls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlshortener",
            name="long_url",
            field=models.URLField(db_index=True, unique=True, verbose_name="Long URL"),
        ),
    ]
