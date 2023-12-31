# Generated by Django 4.2.4 on 2023-09-02 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_milestone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=256)),
                ("description", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                ("completed", models.BooleanField(default=False)),
                ("priority", models.IntegerField(default=0)),
                (
                    "milestone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="main.milestone",
                    ),
                ),
            ],
        ),
    ]
