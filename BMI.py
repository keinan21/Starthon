print("### menghitung BMI ###")
print("_______________________________________")

print("rumus yang digunakan adalah")
print("                             ")
print("      berat badan (kg)")
print("BMI = ________________")
print("      tinggi badan (m)")

print("jika hasil :")
print("- kurang dari 18.5 = underweight")
print("- 18.5 hingga 24.9 = Ideal")
print("- 25.0 hingga 29.9 = Overweight.")
print("- 30.0 ke atas: Obesitas")

print("_______________________________________")
print("                             ")

bb = float(input('masukan nilai berat badan (kg) = '))
tb = float(input('masukan nilai tinggi badan (m) = '))

print("_______________________________________")
print("langkah menghitung")
print(" BMI = berat badan / tinggi badan x tinggi badan")

sementara = tb*tb

print(" BMI =", bb, "/", tb ,"x", tb)
print(" BMI =", bb, "/", sementara)

bmi = bb / sementara

print(" BMI =", bmi)

def hasil(bmi):
    if bmi > 30.0 :
        print("BMI lebih dari 30, masuk kategori obesitas")
    elif bmi > 25.0 :
        print("BMI diantara 25 - 30, masuk kategori overweight")
    elif bmi > 18.5 :
        print("BMI diantara 18.5 - 25, masuk kategori ideal")
    else :
        print("BMI kurang dari 18.5, masuk kategori underweight")

hasil(bmi)






