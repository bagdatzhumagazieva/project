# Generated by Django 2.2 on 2019-05-03 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_ok_answer_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='name',
        ),
    ]
