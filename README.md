# TechSpace
Tautan menuju Aplikasi Adaptable: [TechSpace] (https://techspace.adaptable.app/)

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
![](/image/Bagan%20Request%20Client.jpg)
Setelah urls.py menerima HTTP request dari client, HTTP request akan diarahkan ke path yang sesuai sebelum diteruskan ke views.py. Setelah itu, fungsi view dalam views.py akan memproses data yang sekiranya diperlukan melalui interaksi dengan models.py. Tampilan data yang sudah diperoleh tadi akan diatur berdasarkan template berupa file HTML dan akan dikirimkan kembali kepada client dalam bentuk HTTP response.  

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Iya, kita memang bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, penggunaan virtual environment merupakan salah satu hal yang perlu dibiasakan jika kita sedang membuat lebih dari satu proyek Django di saat yang sama. Dalam praktiknya, setiap proyek bisa saja memiliki versi Python, package, serta dependency yang berbeda-beda. Akibatnya, jika tidak menggunakan virtual environment, proyek-proyek ini bisa saja saling berbentrokan. Oleh karenanya, perlu digunakan virtual environment agar pengembangan aplikasi web berbasis Django ini dapat berlangsung dengan lebih efektif.

## 4. Jelaskan apa itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah pola desain arsitektur yang membagi suatu sistem pengembangan situs web menjadi tiga bagian. Berikut ini adalah penjelasan lebih lengkapnya.

a. MVC terdiri atas Model, View, dan Controller. Model bertugas mengelola data dan menangani logika. View bertugas mengatur tampilan yang akan dilihat oleh user. Controller bertugas mengatur pengolahan data dalam Model serta pengolahan tampilan dalam View.

b. MVT terdiri atas Model, View, dan Template. Model bertugas mengelola data dan menangani logika. View bertugas menerima data dari Model sebelum digunakan di Template. Template bertugas mengatur tampilan yang akan dilihat oleh user.

c. MVVM terdiri atas Model, View, dan ViewModel. Model bertugas mengelola data dan menangani logika. View bertugas mengatur tampilan yang akan dilihat oleh user. ViewModel bertugas sebagai sarana penghubung antara Model dan View.

Perbedaan dari ketiga pola desain ini terletak pada bagaimana ketiganya mengatur hubungan antara data dan tampilan. Pada MVC, Controller bertanggung jawab dalam memberikan perintah untuk pengolahan data di Model serta pengolahan tampilan di View. Pada MVT, pengolahan data dilakukan di Model berdasarkan perintah dari View dan pengolahan tampilan akan diatur di Template. Pada MVVM, adanya ViewModel yang memiliki data binding memungkinkan tampilan langsung diperbarui secara otomatis jika ada data yang diubah.