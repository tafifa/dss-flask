import math

'''
note!!!
program belum bisa untuk data sampel lebih dari 5
mungkin kesalahan di urutan baris dan kolom
bisa coba dari awal lagi
'''

def hitung(data):
    # data = datanp.tolist()
    # print(datanp)
    # print(data)
    sampel = len(data)
    # print(len(data[0]))
    tabel = []

    for baris in range(len(data)):
      sum = 0
      for kolom in range(len(data[0])):
        sum += data[baris][kolom] ** 2
      # print(math.sqrt(sum))
      tabel.append(math.sqrt(sum))
      sum = 0

    # print(tabel)

    tnor = [[0]*(5) for _ in range(sampel)]

    # # tabel matriks ternormalisasi dan terbobot
  
    bobot = [5, 4, 2, 4, 5]

    for baris in range(len(data)):
      for kolom in range(len(data[0])):
        # print(arr[kolom][baris], tabel[kolom])

        hit = data[baris][kolom] / tabel[kolom]
        tnor[baris][kolom] = hit * bobot[kolom]

    # print(tnor)

    tmax = [0] * sampel
    tmin = [0] * sampel

    # print(tnor)

    for baris in range(len(data[0])):
      max = 0
      min = 10
      for kolom in range(len(data)):
        
        if tnor[kolom][baris] > max:
          max = tnor[kolom][baris]

        if tnor[kolom][baris] < min:
          min = tnor[kolom][baris]
      tmax[baris] = max
      tmin[baris] = min
    # print(tmax)
    # print(tmin)

    tKuadratMaks = [[0]*(5) for _ in range(sampel)]
    tKuadratMint = [[0]*(5) for _ in range(sampel)]

    print(tKuadratMaks)
    print('\n')
    print(tKuadratMint)

    for kolom in range(len(data[0])):
      for baris in range(len(data)):
        tKuadratMaks[kolom][baris] = (tmax[baris] - tnor[baris][kolom])**2
        tKuadratMint[kolom][baris] = (tnor[baris][kolom] - tmin[baris])**2

    
    print(tKuadratMaks)
    print('\n')
    print(tKuadratMint)

    tSolMaks = [0] * sampel
    tSolMint = [0] * sampel

    for baris in range(len(data[0])):
      hitMaks = 0
      hitMint = 0
      for kolom in range(len(data)):
        hitMaks += tKuadratMaks[kolom][baris]
        hitMint += tKuadratMint[kolom][baris]
      tSolMaks[baris] = math.sqrt(hitMaks)
      tSolMint[baris] = math.sqrt(hitMint)

    # print(tSolMaks)
    # print('\n')
    # print(tSolMint)
    res = [0] * sampel

    for kolom in range(len(tSolMaks)):
      res[kolom] = tSolMint[kolom]/(tSolMint[kolom] + tSolMaks[kolom])

    return res