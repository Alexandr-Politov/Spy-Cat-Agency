# Generated by Django 5.1.3 on 2024-11-22 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SpyCat",
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
                ("name", models.CharField(max_length=127)),
                ("years_experience", models.PositiveIntegerField()),
                ("breed", models.CharField(max_length=127)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Mission",
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
                ("complete", models.BooleanField(default=False)),
                (
                    "cat",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="missions",
                        to="agency.spycat",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Target",
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
                ("name", models.CharField(max_length=127)),
                ("country", models.CharField(max_length=127)),
                ("notes", models.TextField(blank=True)),
                ("complete", models.BooleanField(default=True)),
                (
                    "mission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="targets",
                        to="agency.mission",
                    ),
                ),
            ],
        ),
    ]
