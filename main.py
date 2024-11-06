# main.py 


# meminta input panjang dan lebar dari pengguna 
def input_posotif(prompt):
    while true:
        try:
            nilai = float(input(prompt))
            if nilai > 0 :
                return nilai 
            else:
                print("nilai harus lebih dari 0. coba lagi.")
        except valueerror:
            print("input tidak valid. masukan angka.")
            

                 
panjang=float(input("masukan panjang "))
lebar=float(input("masukan lebar"))

# menghitung luas
luas= panjang * lebar

# menghitung keliling 
keliling -2 * (panjang + lebar)

#menampilkan hasil luas dan keliling 
print(f"menampilkan hasil luas persegi panjang adalah:{luas}satuan persegi")
print(f"keliling persegi panjang adalah: {keliling}satuan")

