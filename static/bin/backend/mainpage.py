from tkinter import *

# Create the main window
main = Tk()
main.title("Sistem Pendukung Keputusan Golongan UKT Mahasiswa")

nama = Label(main, text="Nama Mahasiswa: ")
nama_entry = Entry(main)

# options C1
pekerjaanOrtu = Label(main, text="Pekerjaan Orang Tua/Wali: ")
pekerjaanOrtu_options = ["PNS", "Swasta", "Tidak Bekerja"]
pekerjaanOrtu_dropdown = OptionMenu(main, StringVar().set(pekerjaanOrtu_options[0]), *pekerjaanOrtu_options)

# options C2
penghasilanOrtu = Label(main, text="Penghasilan Orang Tua/Wali: ")
penghasilanOrtu_options = ["Kurang dari Rp 3.000.000", "Antara Rp 3.000.000 dan Rp 5.000.000", "Lebih dari Rp 5.000.000"]
penghasilanOrtu_dropdown = OptionMenu(main, StringVar().set(penghasilanOrtu_options[0]), *penghasilanOrtu_options)

# options C3
jumlahTanggungan = Label(main, text="Jumlah Tanggungan Orang Tua/Wali: ")
jumlahTanggungan_options = ["1", "2", "3", "Lebih dari 3"]
jumlahTanggungan_dropdown = OptionMenu(main, StringVar().set(jumlahTanggungan_options[0]), *jumlahTanggungan_options)

# options C4
nilaiMasuk = Label(main, text="Nilai Masuk: ")
nilaiMasuk_entry = Entry(main)

# options C5

submit_button = Button(main, text="Submit")

# Define the layout of the form
nama.grid(row=0, column=0, padx=5, pady=5)
nama_entry.grid(row=0, column=1, padx=5, pady=5)

pekerjaanOrtu.grid(row=1, column=0, padx=5, pady=5)
pekerjaanOrtu_dropdown.grid(row=1, column=1, padx=5, pady=5)

penghasilanOrtu.grid(row=2, column=0, padx=5, pady=5)
penghasilanOrtu_dropdown.grid(row=2, column=1, padx=5, pady=5)

jumlahTanggungan.grid(row=3, column=0, padx=5, pady=5)
jumlahTanggungan_dropdown.grid(row=3, column=1, padx=5, pady=5)

nilaiMasuk.grid(row=4, column=0, padx=5, pady=5)
nilaiMasuk_entry.grid(row=4, column=1, padx=5, pady=5)

submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

main.mainloop()
