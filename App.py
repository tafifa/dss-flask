from flask import Flask, render_template, request, redirect, url_for
import csv
from static.python.hitung import hitung
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    nama = request.form['nama']
    jenisPekerjaan = request.form['jenisPekerjaan']
    jumlahPenghasilan = request.form['jumlahPenghasilan']
    x = int(request.form['jumlahTanggungan'])
    jumlahTanggungan = 20 if x < 2 else 40 if x < 3 else 60 if x < 4 else 80 if x < 5 else 100
    jenisRumah = request.form['jenisRumah']
    y = int(request.form['jumlahKendaraan'])
    jumlahKendaraan = 100 if y < 2 else 80 if y < 3 else 60 if y < 4 else 40 if y < 5 else 20
    golongan = 0

    # with open('flaskProj\static\data\data.csv', mode='a', newline='') as file:
    #     fieldnames = ['nama', 'golongan']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writerow({'nama': nama, 'golongan': golongan})

    # with open('flaskproj\static\data\hitung.csv', mode='a', newline='') as file:
    #     fieldnames = ['jenisPekerjaan', 'jumlahPenghasilan', 'jumlahTanggungan', 'jenisRumah', 'jumlahKendaraan']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writerow({'jenisPekerjaan': jenisPekerjaan, 'jumlahPenghasilan': jumlahPenghasilan, 'jumlahTanggungan': jumlahTanggungan, 'jenisRumah': jenisRumah, 'jumlahKendaraan': jumlahKendaraan})

    with open('static\data\data.csv', mode='a', newline='') as file:
        fieldnames = ['nama', 'jenisPekerjaan', 'jumlahPenghasilan', 'jumlahTanggungan', 'jenisRumah', 'jumlahKendaraan', 'golongan']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'nama': nama, 'jenisPekerjaan': jenisPekerjaan, 'jumlahPenghasilan': jumlahPenghasilan, 'jumlahTanggungan': jumlahTanggungan, 'jenisRumah': jenisRumah, 'jumlahKendaraan': jumlahKendaraan, 'golongan': golongan})

    return redirect(url_for('index'))

@app.route('/result')
def result():
    # read data from CSV file
    with open('static\data\data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = [row for row in reader]

    datanp = np.array(data)
    # print(np.array(data)[:, 1:5])
    dataHit = datanp[:, 1:6].astype(int)
    nilaiPref = hitung((dataHit.tolist()))

    print(nilaiPref)

    golongan = [0,0,0,0,0]
    for kolom in range(5):
      x = nilaiPref[kolom]
      # print(x)
      golongan[kolom] = 5 if x < 0.2 else 4 if x < 0.4 else 3 if x < 0.6 else 2 if x < 0.8 else 1

    # print(datanp[:, 6])
    # print(golongan)
    datanp[:, 6] = golongan
    # print(datanp[:, 6])

    # print(nilaiPref)

    # render HTML template and pass data
    return render_template('result.html', data=datanp)

if __name__ == '__main__':
    app.run(debug=True)

'''
masih error kalau input data nda 5

masih error nampilkan data dihitungan karena data nya masih tecampur sama data nama dan hasil golongan # done

jadi aku pisahkan data (nama dan golongan) dan data angka, jadi data angka untuk dihitung # done
'''
