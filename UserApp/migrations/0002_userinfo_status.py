# Generated by Django 3.2.6 on 2021-09-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.CharField(default=101, max_length=20),
            preserve_default=False,
        ),
    ]
