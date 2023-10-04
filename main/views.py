import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# Membuat function view show_main.
@login_required(login_url='/login') # Memastikan halaman main hanya bisa diakses oleh user yang sudah login.
def show_main(request):
    items = Item.objects.filter(user=request.user)
    total_items = items.count() # Menghitung jumlah item.

    context = {
        'app_name': 'TechSpace',
        'name': request.user.username,
        'class': 'PBP D',
        'items': items,
        'last_login': request.COOKIES['last_login'],
        'message': f"You have stored {total_items} items in TechSpace!"
    }

    return render(request, "main.html", context) # Mengembalikan data dalam bentuk HTML.

# Membuat function untuk menambahkan data item.
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

# Mengembalikan data dalam bentuk XML.
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Mengembalikan data dalam bentuk JSON.
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Membuat akun bagi user ketika data di-submit dari form.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Mengautentikasi akun user yang ingin login.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) # Melihat kapan user melakukan login.
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

# Melakukan logout.
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Menambahkan amount suatu item.
def increase_amount(request, id):
    item = Item.objects.get(pk=id)

    if request.method == "POST":
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

# Mengurangi amount suatu item.
def decrease_amount(request, id):
    item = Item.objects.get(pk=id)
    
    if request.method == "POST":
        if item.amount > 0:
            item.amount -= 1
            item.save()
        else:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# Mengubah suatu item.
def edit_item(request, id):
    item = Item.objects.get(pk=id)

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

# Menghapus suatu item.
def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main')) 