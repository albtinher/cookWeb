# Generated by Django 3.2.18 on 2023-06-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]