##belajar phyton

print("### Kalkulator determinan matrix orde 2 ###")
print("___________________________________________")
print("Masukan nilai matrix")
print("     | a b |")
print("A =  | c d |")

a = int(input('masukan nilai  a = '))
b = int(input('masukan nilai  b = '))
c = int(input('masukan nilai  c = '))
d = int(input('masukan nilai  d = '))

print("matrix yang ingin dideterminan")

print("     |", a, b, "|")
print("A =  |", c, d, "|")

print("langkah mnghitung determinan")

print('|A| = ', '(hasil perkalian diagonal utama) - ','(hasil perkalian diagonal samping)')
print('|A| = ', '(', a, 'x', d, ') - ','(', b, 'x', c, ')')

utama = a*d
samping = b*c

print('|A| = ', '(', utama, ') - ','(', samping,')')

hasil_kurang = utama - samping

print('|A| = ', hasil_kurang)