# Generated by Django 4.2.2 on 2023-06-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='address_line_1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
