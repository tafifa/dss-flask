from tkinter import *

# Create the root window
root = Tk()
root.title("Sistem Pendukung Keputusan Golongan UKT Mahasiswa")

# Create the widgets for the form
nama_label = Label(root, text="Nama Mahasiswa:")
nama_entry = Entry(root)

ipk_label = Label(root, text="IPK:")
ipk_entry = Entry(root)

# options = ["Kurang dari Rp 3.000.000", "Antara Rp 3.000.000 dan Rp 5.000.000", "Lebih dari Rp 5.000.000"]
options = [3000000, 4000000, 5000000]

penghasilan_label = Label(root, text="Penghasilan Orang Tua:")
penghasilan_var = StringVar()
penghasilan_var.set(options[0])
penghasilan_dropdown = OptionMenu(root, penghasilan_var, *options)

tanggungan_label = Label(root, text="Jumlah Tanggungan Orang Tua:")
tanggungan_entry = Entry(root)

submit_button = Button(root, text="Submit")

# Define the function to calculate the UKT golongan
def calculate_ukt_golongan():
    nama = nama_entry.get()
    ipk = float(ipk_entry.get())
    penghasilan = float(penghasilan_var.get())
    tanggungan = int(tanggungan_entry.get())

    if ipk >= 3.5:
        if penghasilan <= 3000000:
            if tanggungan <= 2:
                hasil = "Golongan 1"
            elif tanggungan <= 4:
                hasil = "Golongan 2"
            else:
                hasil = "Golongan 3"
        elif penghasilan <= 5000000:
            if tanggungan <= 2:
                hasil = "Golongan 2"
            elif tanggungan <= 4:
                hasil = "Golongan 3"
            else:
                hasil = "Golongan 4"
        else:
            hasil = "Golongan 4"
    elif ipk >= 3.0:
        if penghasilan <= 3000000:
            if tanggungan <= 2:
                hasil = "Golongan 2"
            elif tanggungan <= 4:
                hasil = "Golongan 3"
            else:
                hasil = "Golongan 4"
        elif penghasilan <= 5000000:
            if tanggungan <= 2:
                hasil = "Golongan 3"
            elif tanggungan <= 4:
                hasil = "Golongan 4"
            else:
                hasil = "Golongan 5"
        else:
            hasil = "Golongan 5"
    else:
        hasil = "Tidak mendapatkan UKT"

    # Display the result in a message box
    messagebox.showinfo("Hasil", f"{nama} mendapatkan UKT dengan golongan: {hasil}")

# Attach the function to the submit button
submit_button.config(command=calculate_ukt_golongan)

# Define the layout of the form
nama_label.grid(row=0, column=0, padx=5, pady=5)
nama_entry.grid(row=0, column=1, padx=5, pady=5)

ipk_label.grid(row=1, column=0, padx=5, pady=5)
ipk_entry.grid(row=1, column=1, padx=5, pady=5)

penghasilan_label.grid(row=2, column=0, padx=5, pady=5)
penghasilan_dropdown.grid(row=2, column=1, padx=5, pady=5)

tanggungan_label.grid(row=3, column=0, padx=5, pady=5)
tanggungan_entry.grid(row=3, column=1, padx=5, pady=5)

submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
