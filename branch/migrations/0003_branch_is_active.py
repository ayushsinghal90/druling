# Generated by Django 4.2.17 on 2025-01-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("branch", "0002_branch_img_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
