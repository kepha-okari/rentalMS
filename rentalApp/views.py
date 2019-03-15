from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
# from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.contrib.auth.models import User
from .models import Property, RentalUnit, Tenant

# from  . import config
from django.conf import settings

def index(request):

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_ = request.POST['emailaddress']
        password_ = request.POST['password']
        user =User.objects.create_user(username, email_, password_)
        user.first_name = username.upper()
        user.last_name = username
        user.save()

        authenticated_user = authenticate(username=username, password=password_)
        login(request, authenticated_user)

        # if authenticated_user is not None:
        #     print("Successfully authenticated")
        return redirect(update_profile) # redirect to update profile

    return render(request, 'registration/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username, password=password_)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})


def update_profile(request):
    if request.method == 'POST':

        current_user = request.user
        phone_number = request.POST['phone_number']
        national_id = request.POST['national_id']
        end_date = request.POST['end_date']
        profile_photo = request.POST['imageFile']

        tenant = Tenant.objects.get(user = current_user)
       
        # message = 'Welcome {0}, you have successfully joined RentalMS'.format(current_user)

        tenant.user = current_user
        tenant.phone_number = phone_number
        tenant.national_id = national_id
        tenant.until = end_date
        tenant.profile_photo = profile_photo
        tenant.save()

        # send_messege(message)
    return render(request, 'registration/update_profile.html', {})


def monthly_billing(days, monthly_rate):
    """
    Billing function
    """
    duration = 30 #days in a month 
 
    rent_due = days/duration * int(monthly_rate)
    print("RENT DUE THIS MONTH:{}".format(rent_due))
    return rent_due


# def generate_bulk_invoice():
#     """Generate invoice and notify all tenants when rent is due"""

#     tenants = Tenant.objects.all()

#     for tenant in tenants:
#         number_of_days = Tenant.get_days_difference(tenant.user)
#         monthly_charges = tenant.rental_unit.monthly_rent
#         invoice = monthly_billing(int(number_of_days), int(monthly_charges)
#         # send_message() #send SMS notification to tenants



def generate_specified_invoice(request, current_user):
    """Generate invoice for a specified tenants"""
    current_user = request.user
    tenant = Tenant.objects.get(user = current_user)
    print("Rent:{}".format(int(tenant.rental_unit.monthly_rent)))

    number_of_days = Tenant.get_days_difference(tenant.user) + 20
    monthly_charges = int(tenant.rental_unit.monthly_rent)
    invoice = monthly_billing(number_of_days, monthly_charges)
    print("Days: {}".format(number_of_days))
    print(invoice)
    # send_message()
    return invoice


def view_arrears(request):
    tenant = Tenant.check_arrears(request.user)
    return render(request, 'arrears.html', {"tenant":tenant})


def check_due_rent(request):
    current_user = request.user
    due_rent = generate_specified_invoice(request,current_user)

    print(str(due_rent))

    return render(request, 'rent.html', { "due_rent":due_rent, "current_user":current_user})


# def send_message(request, message):

#     username = config.USERNAME
    
#     api_key = config.API_KEY

#     to = UserProfile.objects.get(user = request.user).phone_number
    
#     message = message

#     gateway = AfricasTalkingGateway(username, api_key)

#     try:
#         results = gateway.sendMessage(to, message)

#         for recipient in results:
#             # status is either "Success" or "error message"
#             print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
#                                                                 recipient['status'],
#                                                                 recipient['messageId'],
#                                                                 recipient['cost']))

#     except AfricasTalkingGatewayException as e:
#         print('Encountered an error while sending: %s' % str(e))


