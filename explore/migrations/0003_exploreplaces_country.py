# Generated by Django 3.2.2 on 2022-03-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0002_exploreplaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='exploreplaces',
            name='country',
            field=models.CharField(default='india', max_length=20),
        ),
    ]
