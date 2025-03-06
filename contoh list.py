kendaraan = ['Vario 160','PCX 160','Genio 150','Hino Dutro 156HD','Supra GTR 150']
vario = [34000000,160,2024,'1200km']
pcx = [36000000,160,2023,'30000km']
genio = [15000000,150,2025,'1500km']
hinodutro = [420000000,4009,2009,'200000km']
supra = [18000000,150,2024,'4000km']

print('Selamat Datang di BRS (Budi Racing Speed)')
print('Daftar Kendaraan :')
print('1.',kendaraan[0])
print('2.',kendaraan[1])
print('3.',kendaraan[2])
print('4.',kendaraan[3])
print('5.',kendaraan[4])

pilih = int(input('Pilih kendaraan berdasarkan nomor : '))

if pilih == 1 :
    print(kendaraan[0])
    print('harga :',vario[0])
    print('cc :',vario[1])
    print('tahun :',vario[2])
    print('odometer :',vario[3])

elif pilih == 2 :
    print(kendaraan[1])
    print('harga :',pcx[0])
    print('cc :',pcx[1])
    print('tahun :',pcx[2])
    print('odometer :',pcx[3])

elif pilih == 3 :
    print(kendaraan[2])
    print('harga :',genio[0])
    print('cc :',genio[1])
    print('tahun :',genio[2])
    print('odometer :',genio[3])

elif pilih == 4 :
    print(kendaraan[3])
    print('harga :',hinodutro[0])
    print('cc :',hinodutro[1])
    print('tahun :',hinodutro[2])
    print('odometer :',hinodutro[3])

elif pilih == 5 :
    print(kendaraan[4])
    print('harga :',supra[0])
    print('cc :',supra[1])
    print('tahun :',supra[2])
    print('odometer :',supra[3])

else :
    print('Input tidak valid')