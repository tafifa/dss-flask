import hitung as t
import numpy as np

sampel = int(input("Masukkan banyak sampel: "))

arr = [[0]*5 for _ in range(5)]

# input
for kolom in range(sampel):
  row = list(map(int, input().split()))
  arr[kolom] = row

# datanp = np.array(arr)

data = t.hitung(arr)
print(data)
# for kolom in range(sampel):
#   x = data[kolom]
#   golongan = 1 if x < 0.2 else 2 if x < 0.4 else 3 if x < 0.6 else 4 if x < 0.8 else 5
#   print(golongan)

'''
80 50 40 60 50
50 60 70 60 40
40 70 80 50 50
50 80 70 90 80
70 90 60 40 80
60 50 60 70 90
50 50 50 50 50
''' 