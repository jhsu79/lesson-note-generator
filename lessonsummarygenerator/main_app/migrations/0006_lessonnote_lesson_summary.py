# Generated by Django 4.2.5 on 2023-09-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_lessonnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonnote',
            name='lesson_summary',
            field=models.TextField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
