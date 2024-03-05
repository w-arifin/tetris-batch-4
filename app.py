# import dari streamlit
import streamlit as st
from PIL import Image
# import dari google colab
import pandas as pd
import os


st.title("Analisis Kepuasan Konsumen Franchise ABD (Ayam Bang Dava)")
st.write("Wondy Arifin || Member of TETRIS Batch IV from DQLAB")

tab1, tab2, tab3 = st.tabs(["Home", "Dataset", "Owl"])
with tab1:

    st.markdown("""
### Latar Belakang
**ABD** kepanjangan dari **Ayam Bang Dava** merupakan salah satu
franchise *fast food* lokal yang populer dengan 
olahan daging ayam kekinian. Populernya adalah hidangan
**"Ayam Geprek"**-nya. 

Ayam geprek di sini disajikan dengan beragam jenis sambal. 
Sambal original dan sambal daun jeruknya paling andalan. 
Seporsinya bisa disajikan dengan nasi putih, nasi merah, 
nasi cabe garam, nasi pedas merah, nasi pedas daun jeruk.
Menu yang banyak dipesan adalah **"Paket Komplit Nasi Ayam Geprek Sambal Matah"**.

***Unique Selling Point*** dari **ABD** ini adalah *fried kailan* yang ada di beberapa
menu makanannya dan juga tersedia sebagai *ala-carte*. *Fried kailan* sebagai pelengkap pada menu
beberapa hidangan ayam geprek mendampingi rasa *crispy* dari ayam geprek
bertemu dengan serat dan gurihnya dari *fried kailan* sehingga menciptakan
perpaduan rasa yang baru.

Seluruh ragam olahan menu tersebut dikemas 
menggunakan piring rotan untuk makan di tempat (*dine-in*), 
dan kotak food grade berwarna merah untuk *takeaway*. 
*Franchise* ini juga menggunakan beberapa aplikasi untuk melakukan pengantaran makanan
agar dapat menjangkau konsumennya. Salah satunya menggunakan layanan **GoFood** dari aplikasi **Gojek**.

Bisnis *fast food* terlihat cukup menguntungkan dibandingkan
dengan bisnis sektor lainnya. Dengan fokus *target market*-nya adalah mahasiswa dan pekerja kantoran.
Tentu dengan harga hidangan murah akan lebih disukai dan banyak diincar oleh konsumen.
Tidak hanya itu, mengusung penjualan makanan dengan konsep "Ayam Geprek" ini bisa dijadikan
sebagai makanan *"comfort-food"* akan sering dibeli karena terjangkau dan banyak hidangan pelengkap
untuk menemani makan.

Dalam kondisi diterpa pandemi tahun 2020, **ABD** menjadi semakin berkembang pesat dan 
hanya berfokus pada konsep *delivery online* atau bisa disebut dengan
*Virtual Restaurant*. Keberhasilan **ABD** di tahun 2020 dan 2021
melahirkan 27 *outlet* yang tersebar di Bandung, Jakarta, Cirebon, dan Tasikmalaya.
Adapun juga *outlet* lainnya yang baru hadir di sekitar Jabodetabek yang akan mendatang di tahun 2024.
""")

    st.divider()

    st.markdown("""
### Rumusan Masalah
Para kompetitor bisnis yang serupa dengan konsep jualan "Ayam Geprek" ini tentu belum
bisa mengungguli kompetitor besar lainnya. Maka dari itu, pentingnya sebuah *product knowledge* dan
*improvement* agar bisa bersaing secara kreatif dan mengusung teknik *marketing* dan *selling* yang bisa mendorong
berkembangnya suatu bisnis dengan harapan konsumen akan melakukan *repeat order*.

Untuk melakukan *improvement* terhadap bisnisnya, tentunya masukan dari konsumen juga sangat berarti
bagi pertumbuhan bisnisnya. Bisnis akan berkembang dan *sustainable* ketika segala *SOP* menjadi suatu acuan
dalam menjalankan suatu bisnis. Hal ini tentunya akan mendapatkan perlakuan yang berbeda yang membuat
faktor ini sulit menjadi pondasi dasar bersama untuk skala *middle manager* dan dibawahnya untuk
mengurusi setiap *outlet* dengan SDM yang beragam. Tentu saja, setiap *outlet* akan ada perbedaannya
dengan *outlet* yang lain dipengaruhi oleh SDM yang dimilikinya serta dari lingkungannya.

Hadirnya suatu *feedback* akan sangat berarti untuk mempertahankan bisnisnya serta mempererat hubungannya antara pelanggan
dan *outlet* terdekatnya agar mendapatkan suatu *improvement* dan perbaikan apabila ada kesalahan dalam memasarkan produknya.
Baik itu mendapatkan respon baik ataupun komentar, tentunya akan mengubah performa dari *franchise* tersebut agar bisa
diterima baik di lingkungan dan kepada masyarakat luas untuk mencoba dan menyantap dari produk ABD ini.
 
Oleh sebab itu, *project* ini berupaya untuk membangun sistem pendukung keputusan dalam menilai suatu produk dan
perbaikan *SOP*, *improvement*, maupun *product knowledge* dari setiap *outlet* agar dapat memiliki kualitas yang sama
sesuai dengan ekspektasi. Pada *project* ini juga dilakukan analisis untuk menguji beberapa hipotesis, di antaranya:
1. Apakah *review* berpengaruh pada penjualan?
2. Apakah sebagian besar *review* mengandung isi kata positif?
3. Seberapa besar pengaruh sebuah *review* terhadap penjualan?
""")
    st.divider()

    st.markdown("""
### Asumsi dan Batasan
Dalam pengerjaan *project* ini, terdapat beberapa asumsi dan batasan di antaranya:

1. Data sebuah *review* yang digunakan untuk analisis diambil dari *website* [GoFood](https://gofood.co.id).
2. Data yang didapatkan hanyalah yang muncul di kolom *review* berupa komentar atau pesan *feedback*.
""")

with tab2:
    st.markdown("""
Sebanyak 28 *outlet* ABD yang tersebar di kawasan Pulau Jawa, data yang berhasil ditarik sebanyak 4000 lebih menggunakan 
*software* Octoparse 8. Data tersebut diambil dan dilakukan *cleaning duplicate* dengan mengambil data *distinct* pada setiap
*outlet*-nya dalam bentuk *file excel (xlsx)*. Data yang didapatkan berupa **nama**, **inisial**, **waktu pembuatan akun**, **rating**,
**review**, **menu**, dan **tanggal pemesanan**. Karena ini melibatkan seluruh cabang, maka semua data yang ditarik akan menambahkan
satu kolom **lokasi** sebagai pembeda untuk masing-masing *outlet*.

""")
    st.image("https://media.discordapp.net/attachments/593140987170390016/1213345865817784380/image.png?ex=65f52365&is=65e2ae65&hm=cfc49466181c8949a711cd36724e54439f079a57634c904e03ef5c67550f25df&=&format=webp", 
             caption="Salah satu contoh review dari ABD outlet Pasar Minggu", use_column_width=True, output_format='auto')

    st.markdown("""
Setelah mendapatkan data dari Octoparse 8 dan di *export* menjadi *file excel*,
data-data tersebut akan kembali diolah agar menjadi satu *dataset* yang akan menjadi patokan agar bisa untuk melakukan analisis dengan
membaginya ke beberapa dataset yang diperlukan untuk dianalisis satu per satu.
Setelah nantinya digabungkan, maka akan ada perubahan kolom yakni:

- Kolom "Title" berubah menjadi "**nama**"
- Kolom "Label" berubah menjadi "**inisial**"
- Kolom "Content" berubah menjadi "**user_since**"
- Kolom "ml1" berubah menjadi "**rating**"
- Kolom "breakword" berubah menjadi "**review**"
- Kolom "ml2" berubah menjadi "**menu**"
- Kolom "Content1" berubah menjadi "**order_date**"
- Kolom "Place" yang ditambahkan melalui *excel* berubah menjadi "**region**"

""")
# ----------------------
# COLAB: Import Dataset
# ----------------------

    direktori = '/dataset/Ayam Bang Dava, Nasi Geprek _ Popcorn, Antapani - GoFood.xlsx'
    df = pd.read_excel(direktori).head(10)
    st.dataframe(df)

