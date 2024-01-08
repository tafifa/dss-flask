import math

sampel = int(input("Masukkan banyak sampel: "))

arr = [[0]*sampel for _ in range(5)]

# input
for kolom in range(5):
  row = list(map(int, input().split()))
  arr[kolom] = row

# tabel matriks pembagi ternormalisasi
tabel = []
for baris in range(len(arr[0])):
  sum = 0
  for kolom in range(len(arr)):
    sum += arr[kolom][baris] ** 2
  # print(math.sqrt(sum))
  tabel.append(math.sqrt(sum))
  sum = 0

# print(tabel)

tnor = [[0]*(sampel) for _ in range(5)]

# # tabel matriks ternormalisasi dan terbobot
bobot = [5, 4, 2, 4, 5]

for baris in range(len(arr[0])):
  for kolom in range(len(arr)):
    # print(arr[kolom][baris], tabel[kolom])

    hit = arr[baris][kolom] / tabel[kolom]
    tnor[baris][kolom] = hit * bobot[kolom]

tmax = [0,0,0,0,0]
tmin = [0,0,0,0,0]

# print(tnor)

for baris in range(len(arr[0])):
  max = 0
  min = 10
  for kolom in range(len(arr)):
    
    if tnor[kolom][baris] > max:
      max = tnor[kolom][baris]

    if tnor[kolom][baris] < min:
      min = tnor[kolom][baris]
  tmax[baris] = max
  tmin[baris] = min
# print(tmax)
# print(tmin)

tKuadratMaks = [[0]*(sampel) for _ in range(5)]
tKuadratMint = [[0]*(sampel) for _ in range(5)]

for kolom in range(len(arr)):
  for baris in range(len(arr[0])):
    tKuadratMaks[kolom][baris] = (tmax[baris] - tnor[kolom][baris])**2
    tKuadratMint[kolom][baris] = (tnor[kolom][baris] - tmin[baris])**2

# print(tKuadratMaks)
# print('\n')
# print(tKuadratMint)

tSolMaks = [0,0,0,0,0]
tSolMint = [0,0,0,0,0]

for baris in range(len(arr[0])):
  hitMaks = 0
  hitMint = 0
  for kolom in range(len(arr)):
    hitMaks += tKuadratMaks[baris][kolom]
    hitMint += tKuadratMint[baris][kolom]
  tSolMaks[baris] = math.sqrt(hitMaks)
  tSolMint[baris] = math.sqrt(hitMint)

# print(tSolMaks)
# print('\n')
# print(tSolMint)

for kolom in range(len(tSolMaks)):
  print(tSolMint[kolom]/(tSolMint[kolom] + tSolMaks[kolom]))

# print(arr)
'''
80 50 40 60 50
50 60 70 60 40
40 70 80 50 50
50 80 70 90 80
70 90 60 40 80
''' 
