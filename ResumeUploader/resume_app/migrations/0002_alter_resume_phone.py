# Generated by Django 4.1.6 on 2023-06-19 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="Phone",
            field=models.PositiveIntegerField(),
        ),
    ]
