# Generated by Django 3.2.7 on 2021-09-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='admitted_by',
            new_name='added_by',
        ),
    ]