from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item

# Membuat function view show_main.
def show_main(request):
    items = Item.objects.all()
    total_items = items.count() # Menghitung jumlah item.

    context = {
        'app_name': 'TechSpace',
        'name': 'Kristoforus Adi Himawan',
        'class': 'PBP D',
        'items': items,
        'message': f"You have stored {total_items} items in TechSpace!"
    }

    return render(request, "main.html", context) # Mengembalikan data dalam bentuk HTML.

# Membuat function untuk menambahkan data item.
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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