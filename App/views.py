from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import Paginator


# Index views here.
def Index(Request):
    page=Request.GET.get('page',1)
    Categories=Paginator(Category.objects.all(), 4).get_page(page)
    Meal=Paginator(Meals.objects.all(), 3).get_page(page)
    return render(Request, 'index.html', {'Meal':Meal,'Categories':Categories})

# Meals views here.
def MealPage(Request):
    page=Request.GET.get('page',1)
    Breakfast=Paginator(Meals.objects.get(Meal_Name="Breakfast").allitems_set.all(),3).get_page(page)
    Lunch=Paginator(Meals.objects.get(Meal_Name="Lunch").allitems_set.all(),3).get_page(page)
    Dinner=Paginator(Meals.objects.get(Meal_Name="Dinner").allitems_set.all(),3).get_page(page)
    return render(Request, 'meals.html',{'all':all,'Breakfast':Breakfast,'Lunch':Lunch,'Dinner':Dinner})

# Food views here.  
def Foodpage(Request):
    page=Request.GET.get('page',1)
    Food=Paginator(Category.objects.get(Category_Name="Food").allitems_set.all(), 6).get_page(page)
    return render(Request, 'Food.html',{'Food':Food})

# Drinks views here. 
def Drinkspage(Request):
    page=Request.GET.get('page',1)
    Drinks=Paginator(Category.objects.get(Category_Name="Drinks").allitems_set.all(), 6).get_page(page)
    return render(Request, 'Drinks.html',{'Drinks':Drinks})

# Sandwich views here. 
def Sandwichpage(Request):
    page=Request.GET.get('page',1)
    Sandwich=Paginator(Category.objects.get(Category_Name="Sandwich").allitems_set.all(), 6).get_page(page)
    return render(Request, 'Sandwich.html',{'Sandwich':Sandwich})

# Snacks views here. 
def Snackspage(Request):
    page=Request.GET.get('page',1)
    Snacks=Paginator(Category.objects.get(Category_Name="Snacks").allitems_set.all(), 6).get_page(page)
    return render(Request, 'Snacks.html',{'Snacks':Snacks})

# Reservation views here. 
def Reservationspage(Request):
    if Request.method == 'POST':
        Names=Request.POST.get('Name')
        Numbers=Request.POST.get('Number')
        Emails=Request.POST.get('Email')
        Dates=Request.POST.get('Date')
        Meal_Names=Request.POST.get('Meal_Name')
        NumberofPeoples=Request.POST.get('NumberofPeople')
        Descriptions=Request.POST.get('Description')
        Forms=Request.POST.get('Form')
        Meal_Names = Meals.objects.get(Meal_Name=Meal_Names)
        if Names and Numbers and Emails and Dates and Meal_Names and NumberofPeoples and Descriptions is not None:
            Reserve=Reservation.objects.create(Name=Names,Number=Numbers,Email=Emails,Date=Dates,Meal_Name=Meal_Names,NumberofPeople=NumberofPeoples, Description=Descriptions)
            Reserve.save()
            messages.success(Request,"Thanks for making your Reservation")
            return redirect(Forms)
        else:
            messages.error(Request,"Not Submited")
            return redirect(Forms)
    return render(Request, 'Reservation.html')

# Order views here. 
def Orderspage(Request):
    if Request.method == 'POST':
        Names=Request.POST.get('Name')
        Numbers=Request.POST.get('Number')
        Emails=Request.POST.get('Email')
        Dates=Request.POST.get('Date')
        Meal_Names=Request.POST.get('Meal_Name')
        Platess=Request.POST.get('Plates')
        DeliveringAddresss=Request.POST.get('DeliveringAddress')
        Descriptions=Request.POST.get('Description')
        Forms=Request.POST.get('Form')
        Meal_Names = Meals.objects.get(Meal_Name=Meal_Names)
        if Names and Numbers and Emails and Dates and Meal_Names and Platess and DeliveringAddresss and Descriptions is not None:
            Orders=Order.objects.create(Name=Names,Number=Numbers,Email=Emails,Date=Dates,Meal_Name=Meal_Names,Plates=Platess,DeliveringAddress=DeliveringAddresss, Description=Descriptions)
            Orders.save()
            messages.success(Request,"Thanks for making your Order")
            return redirect(Forms)
        else:
            messages.error(Request,"Not Submited")
            return redirect(Forms)
    return render(Request, 'Order.html')

# Contact views here. 
def Contacts(Request):
    if Request.method == 'POST':
        Names=Request.POST.get('Name')
        Numbers=Request.POST.get('Number')
        Emails=Request.POST.get('Email')
        Subjects=Request.POST.get('Subject')
        Messages=Request.POST.get('Message')
        Forms=Request.POST.get('Form')
        if Names and Numbers and Emails and Subjects and Messages is not None:
            Contactus=Contact.objects.create(Name=Names,Number=Numbers,Email=Emails,Subject=Subjects,Message=Messages)
            Contactus.save()
            messages.success(Request,"Thanks for contacting us")
            return redirect(Forms)
        else:
            messages.error(Request,"Not Submited")
            return redirect(Forms)
    return render(Request, 'Contactus.html')

def isloged(Request):
    return True if Request.user.is_authenticated else False

# Login views here.
def Adminlog(Request):
    if isloged(Request): return redirect('Index')
    if Request.method == 'POST':
        username=Request.POST.get('username')
        password=Request.POST.get('password')
        log=Request.POST.get('log')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(Request, user)
            is_admin= User.objects.get(username=username).is_superuser
            if is_admin:
                messages.success(Request,f"{Request.user.username}")
                return redirect('Adminpage')
            else:
                messages.success(Request,f"{Request.user.username}")
                return redirect('userpage')
        else:
            messages.error(Request,"Invalid Login Details")
            return redirect(log)
    return render(Request, 'adminlog.html')

# Logout views here.
def Logout(Request):
    auth.logout(Request)
    return redirect('Index')
   
# Adminpage views here.
def Adminpage(Request):
    all=AllItems.objects.all()
    reserve=Reservation.objects.all()
    order=Order.objects.all()
    contact=Contact.objects.all()
    return render(Request, 'Adminpage.html', {'all':all,'reserve':reserve,'order':order,'contact':contact})
# userpage views here.
def userpage(Request):
    all=AllItems.objects.all()
    reserve=Reservation.objects.all()
    order=Order.objects.all()
    contact=Contact.objects.all()
    return render(Request, 'userpage.html', {'all':all,'reserve':reserve,'order':order,'contact':contact})

# Delete views here.
def Deleteall(request, id):
    deletealls=AllItems.objects.get(id=id)
    deletealls.delete()
    return redirect('Adminpage')
def Deletereserve(request, id):
    deletereserves=Reservation.objects.get(id=id)
    deletereserves.delete()
    return redirect('Adminpage')
def Deleteorder(request, id):
    deleteorders=Order.objects.get(id=id)
    deleteorders.delete()
    return redirect('Adminpage')
def Deletecontact(request, id):
    deletecontacts=Contact.objects.get(id=id)
    deletecontacts.delete()
    return redirect('Adminpage')

# Index views here.
def Newsletterview(Request):
    if Request.method == 'POST':
        Email=Request.POST.get('Email')
        News=Request.POST.get('News')
        form= Newsletterform(Request.POST)
        user=Newsletter.objects.filter(Email=Email, Acknowledge=False)
        if user.exists():
            messages.warning(Request, 'You have send us this week newsletter')
        elif form.is_valid():
            form.save()
            messages.success(Request, 'request Submited successfully')
        else:
            messages.error(Request, 'there was an error')
        return redirect (News)
    return HttpResponse('bad request')

def members_name(request):
    
    return render(request,'Members_Name.html')
    
