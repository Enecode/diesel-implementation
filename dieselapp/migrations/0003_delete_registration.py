# Generated by Django 4.2.6 on 2023-10-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dieselapp", "0002_registration"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Registration",
        ),
    ]