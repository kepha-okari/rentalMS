from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# app_name = 'rentalApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('arrears/', views.view_arrears, name='view_arrears'),
    path('rent/', views.check_due_rent, name='check_due_rent'),
    path('tenant/profile/', views.update_profile, name='update_profile'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$',views.user_login,name='login'),

]
