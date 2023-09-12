from django.shortcuts import render

# Membuat fungsi view show_main.
def show_main(request):
    context = {
        'app_name': "TechSpace",
        'name': 'Kristoforus Adi Himawan',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)