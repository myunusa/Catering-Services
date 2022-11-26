from django.urls import path
from .views import *

urlpatterns = [
    path('',Index, name='Index'),
    path('Meals/',MealPage, name='Meals'),
    path('Food/', Foodpage, name='Food'),
    path('Drinks/', Drinkspage, name='Drinks'),
    path('Sandwich/', Sandwichpage, name='Sandwich'),
    path('Snacks/', Snackspage, name='Snacks'),
    path('Reservation/', Reservationspage, name='Reservation'),
    path('Order/', Orderspage, name='Order'),
    path('Contact_us/', Contacts, name='Contact'),    
    path('Adminlog/', Adminlog, name='Adminlog'),
    path('Logout/', Logout, name='Logout'),
    path('Adminpage/', Adminpage, name='Adminpage'),
    path('<int:id>/delete/all/',Deleteall, name='Deleteall'), 
    path('<int:id>/delete/reserve/',Deletereserve, name='Deletereserve'),  
    path('<int:id>/delete/order/',Deleteorder, name='Deleteorder'),  
    path('<int:id>/delete/contact/',Deletecontact, name='Deletecontact'),  
    path('userpage/', userpage, name='userpage'),  
    path('Newsletter/',Newsletterview, name='Newsletter'),
    path('Membersname/',members_name, name='members'),
    
]