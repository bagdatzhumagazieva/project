# Generated by Django 2.2 on 2019-04-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190428_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='title_name',
            new_name='name',
        ),
    ]