# Generated by Django 2.1.5 on 2019-03-14 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(blank=True, max_length=14, null=True)),
                ('property_location', models.CharField(blank=True, max_length=14, null=True)),
                ('property_description', models.CharField(blank=True, max_length=14, null=True)),
                ('property_type', models.CharField(choices=[('R', 'Residential'), ('C', 'Commercial')], default='R', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentalUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_type', models.CharField(choices=[('O', 'One Bed Room'), ('D', 'Two Bed Room'), ('T', 'Three Bed Room'), ('F', 'Four Bed Room'), ('A', 'Class A Office'), ('B', 'Class B Office'), ('C', 'Class C Office')], default='O', max_length=1, null=True)),
                ('monthly_rent', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('is_occupied', models.BooleanField(default=False)),
                ('property_tag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('has_arrears', models.BooleanField(default=False)),
                ('rental_unit', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.RentalUnit')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.Tenant')),
            ],
        ),
    ]
