# Generated by Django 4.2.5 on 2023-09-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(max_length=255),
        ),
    ]
