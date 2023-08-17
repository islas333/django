# Generated by Django 4.2.4 on 2023-08-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_company_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]