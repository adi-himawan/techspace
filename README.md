# TechSpace
Tautan menuju Aplikasi Adaptable: [TechSpace](https://techspace.adaptable.app/)

<details>
<summary> Tugas 2 </summary>

## 1. Jelaskan cara mengimplementasikan proyek di atas secara step-by-step.
1. Membuat direktori dengan nama yang sama dengan repository proyek di GitHub. Sebagai contoh, karena repository ini bernama techspace, maka direktori yang dibuat juga harus bernama techspace. Setelah selesai, tuliskan kode berikut ini di terminal direktori.
```
git init
git branch -M main
git remote add origin
```
2. Membuat dan mengaktifkan virtual environment. Dalam direktori techspace, buka terminal dan tuliskan ```python -m venv env``` untuk membuat virtual environment. Setelah itu, aktifkan dengan menuliskan ```env\Scripts\activate```.
3. Pada direktori yang sama, tulis sejumlah dependency di requirements.txt dan jalankan ```pip install -r requirements.txt``` di terminal.
4. Buat proyek Django baru dengan menuliskan ```django-admin startproject techspace .```.
5. Menambahkan "*" pada ALLOWED_HOSTS di settings.py agar dapat diakses oleh semua host.
6. Menambahkan dokumen .gitignore agar Git mengabaikan file atau direktori tertentu sesuai keperluan.
7. Membuat aplikasi main dengan menjalankan ```python manage.py startapp main```. Setelah itu, tambahkan "main" pada INSTALLED_APPS di settings.py direktori proyek techspace.
8. Melakukan routing agar dapat menjalankan aplikasi main dengan cara membuka urls.py di direktori proyek techspace dan menambahkan kode berikut ini.
```
...
from django.urls import path, include
...
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
9. Membuat model bernama Item pada aplikasi main di models.py. Pada 
proyek ini, model Item memiliki atribut name, amount, description, dan price. Setelah selesai, jalankan perintah berikut ini untuk mengimplementasikan model.
```
python manage.py makemigrations
python manage.py migrate
```
10. Untuk menampilkan nama aplikasi, nama, serta kelas, tambahkan pasangan key-value yang sekiranya dibutuhkan pada views.py di direktori aplikasi main. Pada proyek ini, pasangan key-value yang ditambahkan terdiri atas informasi app_name, name, dan class.
11. Membuat direktori templates pada direktori main dan buatlah file bernama main.html. Pada file main.html, tuliskan kode berikut ini.
```
<h1>{{app_name}} Page</h1>

<h5>Name: </h5>
<p>{{name}}</p>
<h5>Class: </h5>
<p>{{class}}</p>
```
12. Mengonfigurasi routing URL dengan membuka urls.py di direktori main dan tuliskan kode berikut ini.
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
13. Membuat unit testing di tests.py untuk memastikan semuanya sesuai dengan sebagaimana mestinya. Setelah itu, jalankan dengan menuliskan ```python manage.py test``` di terminal.
14. Melakukan push ke repository techspace di GitHub dengan cara menuliskan kode berikut ini.
```
git add *
git commit -m "<pesan_commit>"
git push -u origin main
```
15. Melakukan deployment ke Adaptable. Berikut ini adalah caranya.
- Setelah berhasil login, klik tombol NEW APP dan pilih opsi Connect an Existing Repository.
- Pilih repositori techspace sebagai basis-aplikasi dan pilih branch yang akan dijadikan deployment branch.
- Pilih Python App Template sebagai template deployment.
- Pilih PostgreSQL sebagai tipe basis data.
- Pilih versi Python yang sesuai.
- Pada bagian Start Command, masukkan perintah ```python manage.py migrate && gunicorn techspace.wsgi```.
- Masukkan nama aplikasi untuk domain situs web.
- Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responsnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](/image/Tugas2_BaganRequest.jpg)
Setelah urls.py menerima HTTP request dari client, HTTP request akan diarahkan ke path yang sesuai sebelum diteruskan ke views.py. Setelah itu, fungsi view dalam views.py akan memproses data yang sekiranya diperlukan melalui interaksi dengan models.py. Tampilan data yang sudah diperoleh tadi akan diatur berdasarkan template berupa file HTML dan akan dikirimkan kembali kepada client dalam bentuk HTTP response.  

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Iya, kita memang bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, penggunaan virtual environment merupakan salah satu hal yang perlu dibiasakan jika kita sedang membuat lebih dari satu proyek Django di saat yang sama. Dalam praktiknya, setiap proyek bisa saja memiliki versi Python, package, serta dependency yang berbeda-beda. Akibatnya, jika tidak menggunakan virtual environment, proyek-proyek ini bisa saja saling berbentrokan. Oleh karenanya, perlu digunakan virtual environment agar pengembangan aplikasi web berbasis Django ini dapat berlangsung dengan lebih efektif.

## 4. Jelaskan apa itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah pola desain arsitektur yang membagi suatu sistem pengembangan situs web menjadi tiga bagian. Berikut ini adalah penjelasan lebih lengkapnya.

a. MVC terdiri atas Model, View, dan Controller. Model bertugas mengelola data dan menangani logika. View bertugas mengatur tampilan yang akan dilihat oleh user. Controller bertugas mengatur pengolahan data dalam Model serta pengolahan tampilan dalam View.

b. MVT terdiri atas Model, View, dan Template. Model bertugas mengelola data dan menangani logika. View bertugas menerima data dari Model sebelum digunakan di Template. Template bertugas mengatur tampilan yang akan dilihat oleh user.

c. MVVM terdiri atas Model, View, dan ViewModel. Model bertugas mengelola data dan menangani logika. View bertugas mengatur tampilan yang akan dilihat oleh user. ViewModel bertugas sebagai sarana penghubung antara Model dan View.

Perbedaan dari ketiga pola desain ini terletak pada bagaimana ketiganya mengatur hubungan antara data dan tampilan. Pada MVC, Controller bertanggung jawab dalam memberikan perintah untuk pengolahan data di Model serta pengolahan tampilan di View. Pada MVT, pengolahan data dilakukan di Model berdasarkan perintah dari View dan pengolahan tampilan akan diatur di Template. Pada MVVM, adanya ViewModel yang memiliki data binding memungkinkan tampilan langsung diperbarui secara otomatis jika ada data yang diubah.

</details>

<details>
<summary> Tugas 3 </summary>

## 1. Apa perbedaan antara form POST dan form GET dalam Django?
Salah satu perbedaan form POST dan form GET dalam Django terletak pada cara keduanya mengirimkan data. Pada POST, data dikirimkan melalui request body sehingga data tidak terlihat pada URL. Hal ini membuat POST lebih cocok jika data yang dikirimkan bersifat sensitif. Sementara itu, pada GET, data dikirimkan melalui URL sebagai bagian dari query String. Maka dari itu, GET lebih cocok untuk digunakan jika seorang developer hanya ingin menampilkan data dari server.

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Baik XML maupun JSON adalah dua format pengiriman data terstruktur dari dan ke server yang sering digunakan karena bersifat human-readable sekaligus machine-readable. Perbedaan utama antara keduanya terletak pada struktur data yang digunakan. Struktur data pada XML mirip seperti tree yang memiliki banyak node dan ditandai dengan adanya <>. Berbeda dengan XML, struktur data pada JSON mirip seperti dictionary dalam Python atau berbentuk pasangan key-value.

Sementara itu, berbeda dengan XML dan JSON, HTML lebih banyak digunakan untuk menampilkan data yang didapatkan dari server. Adanya HTML memungkinkan developer untuk mengatur tampilan data yang didapatkan dari server sehingga lebih nyaman untuk dilihat oleh user.

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. Syntax JSON yang relatif lebih singkat dari XML memungkinkan pertukaran data dengan JSON berlangsung secara lebih efisien.
2. Struktur data pada JSON berbentuk pasangan key-value sehingga lebih mudah dibaca oleh manusia.
3. JSON diturunkan dari JavaScript sehingga lebih mudah untuk di-parse di browser.

## 4. Jelaskan cara mengimplementasikan proyek di atas secara step-by-step.
1. Membuat forms.py dalam direktori main dan tuliskan kode berikut ini.
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price"]
```
Sesuaikan isi fields dengan atribut dalam model Item.

2. Melakukan import serta membuat function bernama create_item pada views.py di direktori main. Berikut ini adalah kode yang harus ditambahkan.
```
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ItemForm
from main.models import Item
...
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

3. Mengubah function show_main pada views.py sehingga program dapat mengakses sekaligus menampilkan jumlah object Item yang tersimpan.
```
def show_main(request):
    items = Item.objects.all()
    total_items = items.count()

    context = {
        'app_name': 'TechSpace',
        'name': 'Kristoforus Adi Himawan',
        'class': 'PBP D',
        'items': items,
        'message': f"You have stored {total_items} items in TechSpace!"
    }

    return render(request, "main.html", context)
```

4. Melakukan import create_item dan menambahkan path url ke urlpatterns pada urls.py di direktori main.
```
from main.views import create_item
...
path('create-item', create_item, name='create_item'),
```

5. Dengan memanfaatkan base.html yang sudah dibuat sebelumnya, buat file baru bernama create_item.html pada direktori templates di main. Tuliskan kode berikut ini.
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

6. Dengan memanfaatkan base.html yang sudah dibuat sebelumnya, ubah main.html pada direktori templates di main dengan kode berikut ini.
```
{% extends 'base.html' %}

{% block content %}
    <h1>{{app_name}} Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>

    <br />

    {% comment %} Menambahkan pesan untuk ditampilkan di atas tabel. {% endcomment %}
    <h2>{{message}}</h2> 
    
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Price</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data item di bawah baris ini. {% endcomment %}
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.price}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
{% endblock content %}
```
Selain menampilkan object Item dalam format HTML, kode di atas juga akan menampilkan jumlah object Item yang tersimpan.

7. Membuat function untuk menampilkan semua object Item dalam format XML, XML by ID, JSON, dan JSON by ID di views.py direktori main. Berikut ini adalah kodenya.
```
from django.http import HttpResponse
from django.core import serializers
...
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Dalam kode di atas, serializers digunakan untuk mengembalikan data dalam bentuk XML atau JSON.

8. Melakukan import function untuk menampilkan semua object Item dan tambahkan path url ke urlpatterns di urls.py direktori main. Tuliskan kode berikut ini.
```
from main.views import show_xml, show_xml_by_id, show_json, show_json_by_id
...
path('xml/', show_xml, name='show_xml'),
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/', show_json, name='show_json'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```

## 5. Tampilkan screenshot dari hasil akses URL pada Postman.
1. HTML
![](/image/Tugas3_HTML.jpg)

2. XML
![](/image/Tugas3_XML.jpg)

3. JSON
![](/image/Tugas3_JSON.jpg)

4. XML by ID
![](/image/Tugas3_XMLbyID.jpg)

5. JSON by ID
![](/image/Tugas3_JSONbyID.jpg)

</details>

<details>
<summary> Tugas 4 </summary>

## 1. Jelaskan Django UserCreationForm beserta kelebihan dan kekurangannya.
Django UserCreationForm adalah built-in class-based form dari django.contrib.auth.forms yang ditujukan untuk memudahkan developer dalam membuat formulir untuk registrasi user. Beberapa kelebihan Django UserCreationForm meliputi kemudahan implementasi, adanya sistem validasi otomatis, terintegrasi dengan sistem autentikasi dalam Django, serta dilengkapi dengan fitur keamanan berupa hashing password. Sementara itu, kekurangaan Django UserCreationForm meliputi belum adanya fitur seperti captcha serta terbatasnya field bawaan yang disediakan. Untungnya, kekurangan ini bisa diatasi dengan melakukan customization secara manual.

## 2. Apa perbedaan antara autentikasi serta otorisasi dalam konteks Django? Mengapa keduanya penting?
Autentikasi adalah proses untuk memverifikasi identitas user yang akan login dalam suatu sistem, misalnya melalui username serta password. Sementara itu, otorisasi adalah proses untuk menentukan hak-hak akses yang sekiranya dimiliki oleh seorang user. 

Nyatanya, kedua hal ini memiliki peran yang sama pentingnya. Sebagai "lapisan pertama", proses autentikasi memastikan hanya user yang benar yang masuk ke dalam sistem. Berikutnya, sebagai "lapisan kedua", proses otorisasi memastikan setiap user yang sudah terautentikasi mendapatkan hak akses sesuai dengan "kepentingan" mereka.

## 3. Jelaskan apa itu cookies dalam konteks aplikasi web dan bagaimana Django menggunakan cookies tersebut untuk mengelola data sesi pengguna.
Dalam konteks aplikasi web, cookies adalah data sementara yang disimpan di browser untuk mengelola data user selama web sedang diakses. Saat user pertama kali mengakses web, Django akan membuatkan ID sesi unik bagi user tersebut. ID sesi ini dibuat untuk memastikan data sesi yang diterima user dari server selalu benar. 

Singkatnya, setiap kali browser user melakukan HTTP request ke server, ID sesi akan ikut dikirimkan untuk memastikan data yang diberikan melalui HTTP response sudah benar. Nah, ID sesi ini akan disimpan dalam cookies.

## 4. Dalam pengembangan web, apakah penggunaan cookies aman secara default atau adakah risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web nyatanya tidak 100% aman. Beberapa risiko keamanan potensial yang wajib diwaspadai di antaranya adalah pelacakan oleh third party, cookies hijacking, serta serangan cross-site scripting (XSS). Sebagai salah satu aksi preventif, salah satu hal yang bisa kita lakukan untuk meminimalisir kemungkinan terjadinya risiko potensial ini adalah menggunakan HTTPS.

## 5. Jelaskan bagaimana cara mengimplementasikan proyek di atas secara step-by-step.
1. Mengimplementasikan fitur register.
- Membuka views.py dan tambahkan barisan kode berikut ini untuk membuat function register.
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
...
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
```
Untuk memudahkan pembuatan formulir registrasi user, kita akan menggunakan UserCreationForm bawaan dari Django.

- Membuat file baru bernama register.html pada direktori templates di direktori main. Berikut ini adalah kodenya.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

2. Mengimplementasikan fitur login.
- Membuka views.py dan tambahkan barisan kode berikut ini untuk membuat function login_user.
```
import datetime
from django.contrib.auth import authenticate, login
...
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Barisan kode di atas memungkinkan kita untuk mendata cookies last login user.

- Tambahkan kode berikut ini di atas function show_main views.py.
```
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='/login')
def show_main(request):
    ...
```
Hal ini dilakukan agar halaman main hanya bisa diakses oleh pengguna yang sudah login.

- Membuat file baru bernama login.html pada direktori templates di direktori main. Berikut ini adalah kodenya.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

3. Mengimplementasikan fitur logout.
- Membuka views.py dan tambahkan barisan kode berikut ini untuk membuat function logout_user.
```
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Nantinya, cookies last login akan dihapus setiap kali user melakukan logout.

- Bukalah main.html di direktori templates milik main dan tambahkan barisan kode berikut setelah "Add New Item".
```
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
```

4. Melakukan routing URL di urls.py dengan melakukan import serta menambahkan path url ketiga fitur yang baru dibuat ke urlpatterns.

5. Setelah menjalankan server, manfaatkan halaman-halaman web yang telah dibuat untuk melakukan registrasi user serta membuat item.

6. Untuk menghubungkan model Item dengan User, tambahkan kode berikut ini di models.py.
```
from django.contrib.auth.models import User
...
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Hal ini perlu dilakukan agar item yang dibuat terintegrasi dengan user pembuatnya.

7. Ubahlah kode pada function create_item di views.py agar informasi user yang membuat item juga masuk ke dalam database. Berikut ini adalah kodenya.
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

8. Implementasikan setiap perubahan pada model dengan menjalankan python manage.py makemigrations serta python manage.py migrate.

9. Setelah mengimplementasikan cookies pada login di langkah ke-2, tambahkan kode berikut ini ke dalam function show_main views.py agar cookies last login dapat ditampilkan di halaman main.
```
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```

10. Tambahkan kode berikut sebelum "Add New Item" di main.html direktori templates milik main.
```
 <h5>Last login: {{ last_login }}</h5>
```

11. Tambahkan button untuk increase amount, decrease amount, serta delete item di main.html direktori templates milik main. Setelah itu, buat function yang sesuai untuk masing-masing button di views.py dan lakukan routing di urls.py.

</details>