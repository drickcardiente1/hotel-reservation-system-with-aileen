from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime

def home(request):
    email = request.POST.get('E-mail')
    name = request.POST.get('Name')
    arival = request.POST.get('Arrival')
    departure = request.POST.get('Departure')
    roomType = request.POST.get('RoomType')
    message = request.POST.get('Message')
    price = 0   
    nights=1
    totalN=1
    total = 0
    if roomType =="Budget Room":
        price = 999
 
    if roomType=="Clasic Room":
        price = 1099

    if roomType=="Luxury Room":
        price = 1299
   
    if departure and arival:
        a=parse_datetime(arival)
        d=parse_datetime(departure)
        totalN = d-a
        nights = totalN.days
        total = nights*price
    if email and name and arival and departure:
        Guest.objects.create(Email=email,Name=name,Arival=arival,Departure=departure,RoomType=roomType,Price=price,Nights=nights,Total=total,Message=message)
    return render(request,'users/user.html')

def portal(request):
    return render(request,'admin_section/login.html')

def portalprocces(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('rooms')
    else:
        return render(request,'admin_section/login.html',{
            'error_message' : "Login failed"
        })

def procceslogout(request):
    logout(request)
    return redirect('portal')

@login_required
def homeadmin(request):
    guest = Guest.objects.all()
    paginator = Paginator(guest, 3)
    page_number = request.GET.get('p')
    guest_list = paginator.get_page(page_number)
    context = {'page_obj':guest_list}
    return render(request,'admin_section/home.html',context)

@login_required
def view(request, g_id):
    page_number = request.GET.get('p')
    guest = Guest.objects.all()
    paginator = Paginator(guest, 3)
    guest_list = paginator.get_page(page_number)
    guest_id = Guest.objects.get(id = g_id)
    context = {'page_obj':guest_list,'guest_id':guest_id}
    return render(request,'admin_section/home.html',context)
    
@login_required
def clear_procces(request):
    Guest.objects.all().delete()
    url = 'rooms'
    return redirect('/'+url)

def delete_procces(request, guest_id):
    Guest.objects.filter(id = guest_id).delete()
    url = 'rooms'
    return redirect('/'+url)
    
    