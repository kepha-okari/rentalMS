from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
from datetime import timedelta

class Property(models.Model):

    PROPERTY_TYPE_CHOICES = (
        ('R', 'Residential'),
        ('C', 'Commercial'),
    )

    property_name = models.CharField(max_length=50, blank=True, null=True)
    property_location = models.CharField(max_length=50, blank=True, null=True)
    property_description = models.CharField(max_length=200, blank=True, null=True)
    property_type = models.CharField(max_length=1, choices=PROPERTY_TYPE_CHOICES, null=True, default='R')

    def __str__(self):
        return self.property_name
    





class RentalUnit(models.Model):

    UNIT_TYPE_CHOICES = (
        ('O', 'One Bed Room'),
        ('D', 'Two Bed Room'),
        ('T', 'Three Bed Room'),
        ('F', 'Four Bed Room'),
        ('A', 'Class A Office'),
        ('B', 'Class B Office'),
        ('C', 'Class C Office'),
    )
    unit_name = models.CharField(max_length=100, blank=True, null=True)
    unit_description = models.CharField(max_length=100, blank=True, null=True)
    unit_type = models.CharField(max_length=1, choices=UNIT_TYPE_CHOICES, null=True, default='O')
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_occupied = models.BooleanField(default=False)
    property_tag = models.ManyToManyField(Property, related_name = "property_tag")



    def __str__(self):
    	return self.unit_name






class Tenant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    rental_unit = models.OneToOneField(RentalUnit,on_delete=models.CASCADE, blank=True, null=True)
    as_from =  models.DateField(auto_now_add=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    profile_photo = models.ImageField(upload_to = 'profile/', default='profile/default.jpg')
    until =  models.DateField( blank=True, null=True)
    has_arrears = models.BooleanField(default=False)
    has_vacated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_tenant(cls, user_id):
        tenant = cls.objects.get(user=user_id)
        return tenant 
    
    @classmethod
    def check_arrears(cls, user_id):
        tenant = cls.objects.filter(user=user_id, has_arrears = True)
        return tenant
    

    

    @classmethod
    def get_days_difference(cls, tenant_id):
        """
        Funtion that find the difference in days for monthly billing
        """
        tenant = cls.objects.get(user = tenant_id, has_vacated = False)

        start_date = tenant.as_from
        end_date =  tenant.until

        difference_in_days = abs(end_date - start_date).days

        return difference_in_days



@receiver(post_save, sender=User)
def create_tenant(sender, **kwargs):
    if kwargs['created']:
        Tenant.objects.create(user=kwargs['instance'])

post_save.connect(create_tenant, sender=User)


