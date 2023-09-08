import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    no_tlp = entry_no_tlp.get()
    alamat = entry_alamat.get()
    
    
    messagebox.showinfo("Info", "Data siswa berhasil disimpan ke Data")

root = tk.Tk()
root.title("Aplikasi Data Siswa")

label_nama = tk.Label(root, text="Nama+")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_tanggal_lahir = tk.Label(root, text="Tanggal Lahir")
label_tanggal_lahir.grid(row=1, column=0)
entry_tanggal_lahir = tk.Entry(root)
entry_tanggal_lahir.grid(row=1, column=1)

label_asal_sekolah = tk.Label(root, text="Asal Sekolah")
label_asal_sekolah.grid(row=2, column=0)
entry_asal_sekolah = tk.Entry(root)
entry_asal_sekolah.grid(row=2, column=1)

label_nisn = tk.Label(root, text="NISN")
label_nisn.grid(row=3, column=0)
entry_nisn = tk.Entry(root)
entry_nisn.grid(row=3, column=1)

label_nama_ayah = tk.Label(root, text="Nama Ayah")
label_nama_ayah.grid(row=4, column=0)
entry_nama_ayah = tk.Entry(root)
entry_nama_ayah.grid(row=4, column=1)

label_nama_ibu = tk.Label(root, text="Nama Ibu")
label_nama_ibu.grid(row=5, column=0)
entry_nama_ibu = tk.Entry(root)
entry_nama_ibu.grid(row=5, column=1)

label_no_tlp = tk.Label(root, text="No. Telepon")
label_no_tlp.grid(row=6, column=0)
entry_no_tlp = tk.Entry(root)
entry_no_tlp.grid(row=6, column=1)

label_alamat = tk.Label(root, text="Alamat")
label_alamat.grid(row=7, column=0)
entry_alamat = tk.Entry(root)
entry_alamat.grid(row=7, column=1)

button_simpan = tk.Button(root, text="Simpan", command=simpan_data)
button_simpan.grid(row=8, columnspan=2)

root.mainloop()