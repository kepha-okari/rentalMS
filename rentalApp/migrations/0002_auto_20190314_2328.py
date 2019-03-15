# Generated by Django 2.1.5 on 2019-03-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='date_posted',
            new_name='as_from',
        ),
        migrations.AddField(
            model_name='tenant',
            name='until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
