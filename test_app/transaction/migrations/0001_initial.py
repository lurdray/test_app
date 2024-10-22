# Generated by Django 5.0.3 on 2024-10-22 05:51

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("sender", models.CharField(default=None, max_length=255)),
                ("receiver", models.CharField(default=None, max_length=255)),
                ("amount", models.FloatField(default=None, max_length=255)),
                ("status", models.BooleanField(default=False)),
                ("pub_date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]