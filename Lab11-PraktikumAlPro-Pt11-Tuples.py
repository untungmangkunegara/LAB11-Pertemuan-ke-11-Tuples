# 71200619 Untung Mangkunegara

# Materi Tuples
# Referensi: UG 11 GRUP C nomor 2
# Uun adalah seorang bendahara suatu event yang penting di sekolahnya. Dia ingin menghitung semua pengeluaran dari tiap divisi
# namun karena iseng dia ingin membuat program perhitungan secara tuple untuk menjumlahkan keseluruhan pengeluarannya. 
# Bantulah Uun untuk membuatkan program yang sesuai.

divisi=("Inti","Sponsorship","Usaha Dana","Environment","Perlengkapan","Dokumentasi","Dekorasi","L.O","Stand","Humas","Venue","P3K","Keamanan")

def pengeluarandivisi(x):
    totalpengeluaran=0
    for i in x:
        pengeluaran=int(input("Masukkan pengeluaran Divisi "+i+" : Rp."))
        totalpengeluaran=totalpengeluaran+pengeluaran
    print("Total pengeluaran semua divisi adalah Rp.",totalpengeluaran)

pengeluarandivisi(divisi)

# Sindu ingin mencari irisan dari dua buah tuple yang dimilikinya. Akan tetapi, Sindu
# terkadang kurang teliti dalam melakukan hal seperti ini. Oleh sebab itu, bantulah
# Sindu membuat program untuk mencari irisan dari dua buah tuple karena anda
# adalah teman baik Sindu dan seorang programmer yang handal!
# Catatan : Output terakhir yang dikeluarkan harus berupa Tuple!!
# UG KELAS C NOMOR 4

tup1=(1,2,3,4)
tup2=(3,2,4,1)
tup3=(1,)
tup4=(1,3,5,7,9)

def irisan(y,z):
    a=set(y)
    b=set(z)
    c=a.intersection(b)
    print("Irisan kedua tuple tersebut adalah: ",c)

irisan(tup1,tup2)
irisan(tup3,tup1)
irisan(tup2,tup4)