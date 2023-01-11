# Fungsi untuk daftar_CLO yang diminta yang didalamnya terdapat parameter file
def daftar_clo(file):
    # Membuka file text
    file = open(file, "r")

    # inisialisasi variabel
    clo = dict()
    nilai = dict()
    daftar_clo = dict()

    # Perulangan untuk memanggil file text menjadi bentuk string
    for i in file.readlines():

        list = i.split()
        nim = list[0]

        # Menjadikan file text ke bentuk dictionary
        clo[nim] = [int(j) for j in list[1:]]

    # Menutup File text
    file.close()

    # Perulangan untuk inisialisasi key awal dari dict  variable nilai dan daftar_clo untuk mengelompokkan nilai clo
    for i in range(len(list[1:])):
        nilai[i+1] = []
        daftar_clo[f'CLO {i+1}'] = []

    # Perulangan untuk mengelompokkan nilai clo
    for i in range(len(list[1:])):

        # Perulangan untuk memanggil key dari dict variable nilai
        for k in nilai.keys():
            # Perulangan untuk memanggil value dari dict variable clo
            for v in clo.values():
                # pengecekan kondisi key dari dict variable nilai
                if i+1 == k:
                    # pengelompokan nilai clo
                    nilai[k].append(v[i])

    # Perulangan untuk memisahkan key dan value dari dict variable nilai
    for k, v in nilai.items():
        # Inisialisasi jumlah mahasiswa di bawah standar nilai kelulusan
        lima_puluh = 0

        # Perulangan untuk memecah value dari dict variable nilai
        for i in v:
            # Pengecekan jika nilai dibawah stardar kelulusan
            if i <= 50:
                lima_puluh += 1

        # Memasukkan value yang diinginkan ke dict variable daftar_clo
        daftar_clo[f'CLO {k}'].append(round(sum(v)/len(v), 2))
        daftar_clo[f'CLO {k}'].append(max(v))
        daftar_clo[f'CLO {k}'].append(min(v))
        daftar_clo[f'CLO {k}'].append(lima_puluh)

    # Mengembalikan nilai
    return daftar_clo


# Fungsi untuk menampilkan data setiap CLO sesuai dengan dictionary yang telah di buat dan terdapat parameter data

def report(data):
    # Perulangan untuk menampikan data clo
    for k, v in data.items():
        print("=========")
        print(k)
        print("=========")
        print(f"Rerata {k} semua mahasiswa : {v[0]}")
        print(f"Nilai {k} tertinggi : {v[1]}")
        print(f"Nilai {k} terendah : {v[2]}")
        print(
            f"Jumlah mahasiswa di bawah standar kelulusan {k} : {v[3]} orang")
        print("")


# Main program
daftar_CLO = daftar_clo('file.txt')
report(daftar_CLO)
