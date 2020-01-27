# Backend Pendataan Jamaah Wirid Khusus NW
## Introduction
Aplikasi merupakan aplikasi untuk pendataan Jamaah Wirid Khusus NW di seluruh Indonesia. Aplikasi ini merupakan aplikasi bagian belakang/Backend yang akan mengurus proses pendataan (CRUD) data Jamaah. Aplikasi ini dibuat dengan menggunakan bahasa pemrograman [Python](https://docs.python.org/).

Aplikasi ini bisa diakses di URL [SIMJAWI](http://117.53.47.113/)

### Cara Instalasi Backend
Untuk melakukan instalasi aplikasi ini ada beberapa hal yang harus dipersiapkan:
* Pastikan Git sudah terinstall di perangkat anda
* Pastikan bahwa python yang terinstall di perangkat anda merupakan ```python >= 3.7```
* Pastikan anda telah memasang ```virtualenv``` untuk mengatur library yang digunakan nantinya.

Setelah point di atas sudah siap, berikut langkah-langkah instalasinya:
* Unduh/clone repository

    ```git clone https://github.com/ganggas95/jamaah_nw_be.git``` 
    
    atau

    ```git clone git@github.com:ganggas95/jamaah_nw_be.git```

* Masuk ke folder project
* Buat virtual environment menggunakan perintah ```virtualenv -p python3.7 venv```  lalu aktifkan menggunakan perintah ```source venv/bin/activate```
* Install library yang digunakan oleh project dengan perintah ```pip install -r requirements.txt```
* Ubah file ```.env``` bagian ```DATABASE_URI``` dan sesuaikan dengan database connection yang anda gunakan
* Jalankan ```python app.py```

### Menjalankan Celery
Celery di dalam project ini digunakan untuk mengkalkulasi data jamaah untuk dijadikan report excel secara asyncronous untuk menanggulangi request timeout ketika data yang diproses memiliki kapasitas data yang besar.

Sebelum menjalankan celery berikut hal yang perlu disiapkan:
1. Pastikan sudah terinstall redis-server dan berjalan dengan baik

Langkah-langkah menjalankan celery:
1. Aktifkan virtualenv dengan cara seperti cara sebelumnya
2. Jalankan perintah ```./bin/celery_runner.sh```


### Harapan kami sebagai developer (pengembang aplikasi ini)

Aplikasi ini merupakan aplikasi persembahan dari murid-murid Maulana Syaikh TGKH. Muhammad Zainuddin Abdul Majid untuk mempermudah dalam pendataan jamaah wirid khusus yang saat ini terdata dalam bentuk hard copy mencapai 20ribuan data lama, belum termasuk data baru. Jadi harapan kami dengan aplikasi ini dapat dipergunakan sebagaimana mestinya. Dan ada ide-ide kedepannya untuk pengembangan aplikasi ini sehingga data yang terkumpul menjadi data yang berkualitas dan dapat bermanfaat dengan baik.

Semoga Allah Meridhoi segala bentuk usaha/ikhtiar kita. Amin Ya Robbal 'Alamin.

