# Generated by Django 4.0.4 on 2022-05-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]