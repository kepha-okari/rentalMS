# Generated by Django 2.1.5 on 2019-03-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0008_auto_20190315_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenantprofile',
            name='tenant',
        ),
        migrations.AddField(
            model_name='tenant',
            name='national_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='TenantProfile',
        ),
    ]
