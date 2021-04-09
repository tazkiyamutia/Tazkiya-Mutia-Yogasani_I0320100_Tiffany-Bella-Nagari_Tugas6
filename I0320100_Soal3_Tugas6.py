# Soal 3 Tugas 6

def cekPrime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                print(x, "bukan prima")
                break
        else :
            print(x, "adalah bilangan prima")
    else :
        print(x, "bukan prima")


awal = 10
akhir  = 24

for j in range(awal, akhir+1):
    cekPrime(j)