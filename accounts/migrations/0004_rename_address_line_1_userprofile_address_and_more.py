# Generated by Django 4.2.2 on 2023-06-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_address_userprofile_address_line_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line_1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_2',
        ),
    ]