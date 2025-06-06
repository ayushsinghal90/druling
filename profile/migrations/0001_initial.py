# Generated by Django 4.2.15 on 2024-12-31 16:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "img_url",
                    models.URLField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Profile Image URL",
                    ),
                ),
                (
                    "contact",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to="contact.contact",
                    ),
                ),
            ],
            options={
                "db_table": "profile",
            },
        ),
    ]
