class Contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = namaself
        self.nomor_telepon = nomor_telepon
        self.email = email

        def tampilkan_info(self):
            print(f"Nama: {self.nama}")
            print(f"Nomor Telepon: {self.nomor_telepon}")
            print(f"Email: {self.email}")
            print()


class AddressBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilkan_semua_kontak(self):
        print("Daftar Kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

    