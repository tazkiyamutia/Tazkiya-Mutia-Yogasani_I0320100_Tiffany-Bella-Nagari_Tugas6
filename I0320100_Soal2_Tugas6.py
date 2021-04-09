# Soal 2 Tugas 6

jumlah_data = int(input('Masukkan jumlah data : '))
list_nilai = []
total = 0
# print(list_nilai)
for i in range(jumlah_data):
    nilai = int(input('Masukkan nilai : '))
    list_nilai.append(nilai)
    # print(list_nilai)
# print(list_nilai)
for i in list_nilai:
    total = total + i
# print(total)
rata_rata = total/jumlah_data
print('Rata-rata data adalah : ', rata_rata)