# Generated by Django 2.2.20 on 2021-05-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20210505_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='language_code',
            field=models.CharField(default='en', max_length=50),
        ),
    ]
