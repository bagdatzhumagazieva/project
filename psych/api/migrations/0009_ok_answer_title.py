# Generated by Django 2.2 on 2019-05-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190503_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='ok_answer',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Title'),
        ),
    ]
