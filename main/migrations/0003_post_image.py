# Generated by Django 3.1 on 2020-08-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_auto_20200831_2040"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
