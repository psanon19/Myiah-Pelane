# Generated by Django 2.0.6 on 2018-12-05 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='QuestionModel',
        ),
    ]