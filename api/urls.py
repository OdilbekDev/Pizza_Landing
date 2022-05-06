from django.urls import path
from api.urls import *
from .views import *
urlpatterns = [
    path('get-slider/', Get_Slider),
    path('get-info/', Get_Info),
    path('get-welcome/', Get_Welcome),
    path('get-service/', Get_Service),
    path('get-hots/', Get_Hots),
    path('get-pricing/', Get_Pricing),
    path('get-achievement/', Get_Achievement),
    path('filter-category/', Filter_Category),
    path('get-blog/', Get_Blog),
    path('filter-blog/', Filter_Blog),
    path('create-contact/', Create_Contact),
    path('add-cart/', Add_Cart),
    path('del-cart/', Del_Cart),
    path('get-cart/', Get_Cart),
    path('add-order/', Add_Order),
    path('get-order/', Get_Order)
]