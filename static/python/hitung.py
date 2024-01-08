import math

def hitung(data):
    # data = datanp.tolist()
    # print(datanp)
    # print(data)
    sampel = len(data)
    tabel = []
    for baris in range(len(data[0])):
      sum = 0
      for kolom in range(len(data)):
        sum += data[kolom][baris] ** 2
      # print(math.sqrt(sum))
      tabel.append(math.sqrt(sum))
      sum = 0

    # print(tabel)

    tnor = [[0]*(sampel) for _ in range(5)]

    # # tabel matriks ternormalisasi dan terbobot
    # bobot = [5, 4, 2, 4, 5]
    bobot = [2, 5, 3, 3, 2]

    for baris in range(len(data[0])):
      for kolom in range(len(data)):
        # print(data[kolom][baris], tabel[kolom])

        hit = data[baris][kolom] / tabel[kolom]
        tnor[baris][kolom] = hit * bobot[kolom]

    tmax = [0,0,0,0,0]
    tmin = [0,0,0,0,0]

    print("Tabel Ternormalisasi Terbobot")
    print(tnor)

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
    print("Nilai Maks",tmax)
    print("Nilai Min",tmin)

    tKuadratMaks = [[0]*(sampel) for _ in range(5)]
    tKuadratMint = [[0]*(sampel) for _ in range(5)]

    for kolom in range(len(data)):
      for baris in range(len(data[0])):
        tKuadratMaks[kolom][baris] = (tmax[baris] - tnor[kolom][baris])**2
        tKuadratMint[kolom][baris] = (tnor[kolom][baris] - tmin[baris])**2

    # print("Jarak Antara Alternatif Solusi Positif",tKuadratMaks)
    # print('\n')
    # print("Jarak Antara Alternatif Solusi Negatif",tKuadratMint)

    tSolMaks = [0,0,0,0,0]
    tSolMint = [0,0,0,0,0]

    for baris in range(len(data[0])):
      hitMaks = 0
      hitMint = 0
      for kolom in range(len(data)):
        hitMaks += tKuadratMaks[baris][kolom]
        hitMint += tKuadratMint[baris][kolom]
      tSolMaks[baris] = math.sqrt(hitMaks)
      tSolMint[baris] = math.sqrt(hitMint)

    print("Jarak Antara Alternatif Solusi Positif",tSolMaks)
    print('\n')
    print("Jarak Antara Alternatif Solusi Negatif",tSolMint)

    # print(tSolMaks)
    # print('\n')
    # print(tSolMint)
    res = [0,0,0,0,0]

    for kolom in range(len(tSolMaks)):
      res[kolom] = tSolMint[kolom]/(tSolMint[kolom] + tSolMaks[kolom])

    print("Nilai Preferensi, res")
    return res