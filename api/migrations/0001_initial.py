# Generated by Django 4.0.1 on 2022-01-28 16:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_code', models.CharField(blank=True, max_length=255)),
                ('category_title', models.CharField(blank=True, max_length=255)),
                ('diagnosis_code', models.CharField(blank=True, max_length=255)),
                ('full_code', models.CharField(blank=True, max_length=255)),
                ('abbreviated_description', models.CharField(blank=True, max_length=255)),
                ('full_description', models.TextField(blank=True)),
                ('added_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
