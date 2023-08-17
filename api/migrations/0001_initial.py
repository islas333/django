# Generated by Django 4.2.4 on 2023-08-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("website", models.URLField(max_length=100)),
                ("foundation", models.PositiveIntegerField()),
            ],
        ),
    ]
