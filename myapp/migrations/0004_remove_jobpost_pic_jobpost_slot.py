# Generated by Django 4.0.4 on 2022-05-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_jobpost_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='pic',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='slot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]