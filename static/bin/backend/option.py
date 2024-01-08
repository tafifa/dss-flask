from tkinter import *

def inputLabel(main):
  nama = Label(main, text="Nama Mahasiswa: ")
  nama_entry = Entry(main)

  # options C1
  pekerjaanOrtu = Label(main, text="Pekerjaan Orang Tua/Wali: ")
  pekerjaanOrtu_options = ["PNS", "Swasta", "Tidak Bekerja"]
  pekerjaanOrtu_dropdown = OptionMenu(main, StringVar.set(pekerjaanOrtu_options[0]), *pekerjaanOrtu_options)

  # options C2
  penghasilanOrtu = Label(main, text="Penghasilan Orang Tua/Wali: ")
  penghasilanOrtu_options = ["Kurang dari Rp 3.000.000", "Antara Rp 3.000.000 dan Rp 5.000.000", "Lebih dari Rp 5.000.000"]
  penghasilanOrtu_dropdown = OptionMenu(main, StringVar.set(penghasilanOrtu_options[0]), *penghasilanOrtu_options)

  # options C3
  jumlahTanggungan = Label(main, text="Jumlah Tanggungan Orang Tua/Wali: ")
  jumlahTanggungan_options = ["1", "2", "3", "Lebih dari 3"]
  jumlahTanggungan_dropdown = OptionMenu(main, StringVar.set(jumlahTanggungan_options[0]), *jumlahTanggungan_options)

  # options C4
  nilaiMasuk = Label(main, text="Nilai Masuk: ")
  nilaiMasuk_entry = Entry(main)

  # options C5
  

  return nama_entry, pekerjaanOrtu_dropdown, penghasilanOrtu_dropdown, jumlahTanggungan_dropdown, jumlahTanggungan_dropdown, nilaiMasuk_entry