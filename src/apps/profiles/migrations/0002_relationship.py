# Generated by Django 4.2.4 on 2023-08-22 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Relationship",
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
                (
                    "status",
                    models.CharField(
                        choices=[("send", "send"), ("accepted", "accepted")],
                        max_length=8,
                    ),
                ),
                ("updated", models.DateField(auto_now=True)),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to="profiles.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="profiles.profile",
                    ),
                ),
            ],
        ),
    ]