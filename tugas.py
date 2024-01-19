def menuPilihan(NimList, NilaiMahasiswa, NilaiIndeks):
    print("Menu Pilihan:")
    print("1. Tampilkan Tabel")
    print("2. Tambah Data Mahasiswa")
    print("3. Tambah Mata Kuliah")
    print("4. Hapus Data Mahasiswa")
    print("5. Ubah Nilai")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan (0-5): "))

    match pilihan:
        case 0:
            print("Program selesai.")
        case 1:
            TampilTabel(NimList, NilaiMahasiswa, NilaiIndeks)
        case 2:
            TambahData(NimList, NilaiMahasiswa, NilaiIndeks)
        case 3:
            TambahMataKuliah(NilaiMahasiswa, NimList)
        case 4:
            HapusData(NimList, NilaiMahasiswa, NilaiIndeks)
        case 5:
            UbahNilai(NimList, NilaiMahasiswa, NilaiIndeks)
        case _:
            print("Pilihan tidak valid.")



def TambahData(NimList, NilaiMahasiswa, NilaiIndeks):
    nim = input("Masukkan NIM mahasiswa: ")

    # Periksa apakah NilaiMahasiswa kosong
    if not NilaiMahasiswa:
        # Jika kosong, minta jumlah mata kuliah dan atur panjangnya sesuai
        NumMatkul = int(input("Masukkan jumlah mata kuliah: "))
        NilaiMatkul = [0] * NumMatkul
    else:
        # Jika tidak kosong, set panjangnya berdasarkan jumlah mata kuliah yang sudah ada
        NilaiMatkul = [0] * len(NilaiMahasiswa[0])

    for j in range(len(NilaiMatkul)):
        nilai = int(input(f"Masukkan nilai mata kuliah {j+1} untuk mahasiswa: "))
        NilaiMatkul[j] = HitungIndeksNilai(nilai)

    NimList.append(nim)
    NilaiMahasiswa.append(NilaiMatkul)
    NilaiIndeks.append(HitungIp(NilaiMatkul))

    print("Data mahasiswa berhasil ditambahkan!")


def TambahMataKuliah(NilaiMahasiswa, NimList):
    # Periksa apakah NilaiMahasiswa kosong
    if not NilaiMahasiswa:
        print("Belum ada data mahasiswa. Tambah data mahasiswa terlebih dahulu.")
        return

    # Minta input mata kuliah baru untuk setiap mahasiswa
    for i in range(len(NilaiMahasiswa)):
        nilai = int(input(f"Masukkan nilai mata kuliah baru untuk mahasiswa {NimList[i]}: "))
        NilaiMahasiswa[i].append(HitungIndeksNilai(nilai))

    print("Mata kuliah berhasil ditambahkan!")


    # Minta input mata kuliah baru untuk setiap mahasiswa
    for i in range(len(NilaiMahasiswa)):
        nilai = int(input(f"Masukkan nilai mata kuliah baru untuk mahasiswa {NimList[i]}: "))
        NilaiMahasiswa[i].append(HitungIndeksNilai(nilai))

    print("Mata kuliah berhasil ditambahkan!")

def HapusData(NimList, NilaiMahasiswa, NilaiIndeks):
    # Periksa apakah ada data mahasiswa
    if not NimList:
        print("Tidak ada data mahasiswa yang bisa dihapus.")
        return

    # Mintalah indeks data mahasiswa yang ingin dihapus
    indeks = int(input("Masukkan indeks data mahasiswa yang ingin dihapus: "))

    # Periksa apakah indeks valid
    if 1 <= indeks <= len(NimList):
        del NimList[indeks - 1]
        del NilaiMahasiswa[indeks - 1]
        del NilaiIndeks[indeks - 1]
        print("Data mahasiswa berhasil dihapus!")
    else:
        print("Indeks tidak valid.")

def UbahNilai(NimList, NilaiMahasiswa, NilaiIndeks):
    nim = input("Masukkan NIM mahasiswa yang nilai mata kuliahnya ingin diubah: ")

    for i in range(len(NimList)):
        if nim == NimList[i]:
            for j in range(len(NilaiMahasiswa[i])):
                nilai = int(input(f"Masukkan nilai mata kuliah {j+1} untuk mahasiswa {nim}: "))
                NilaiMahasiswa[i][j] = HitungIndeksNilai(nilai)

            NilaiIndeks[i] = HitungIp(NilaiMahasiswa[i])
            print("Nilai mata kuliah berhasil diubah!")
            return

    print("NIM tidak ditemukan!")

def HitungIndeksNilai(nilai):
    if nilai >= 80:
        return 'A'
    elif nilai >= 70:
        return 'B'
    elif nilai >= 60:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

def HitungIp(NilaiMahasiswa):
    total_sks = 0
    total_bobot = 0

    for nilai in NilaiMahasiswa:
        bobot = 0

        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1

        total_sks += 1
        total_bobot += bobot

    if total_sks == 0:
        return 0
    else:
        return round(total_bobot / total_sks, 2)


def TampilTabel(NimList, NilaiMahasiswa, NilaiIndeks):
    print("NIM\tMK 1\tMK 2\tMK 3\tMK 4\tIP")

    for i in range(len(NimList)):
        print(f"{NimList[i]}\t", end="")
        for j in range(len(NilaiMahasiswa[i])):
            print(f"{NilaiMahasiswa[i][j]}\t", end="")
        print(f"{NilaiIndeks[i]}\t")


def main():
    M = int(input("Masukkan jumlah mahasiswa: "))
    N = int(input("Masukkan jumlah mata kuliah: "))

    NimList = []
    NilaiMahasiswa = []
    NilaiIndeks = []

    for i in range(M):
        nim = input(f"Masukkan NIM mahasiswa {i+1}: ")
        NilaiMatkul = []

        for j in range(N):
            nilai = int(input(f"Masukkan nilai mata kuliah {j+1} untuk mahasiswa {i+1}: "))
            NilaiMatkul.append(HitungIndeksNilai(nilai))

        NimList.append(nim)
        NilaiMahasiswa.append(NilaiMatkul)
        NilaiIndeks.append(HitungIp(NilaiMatkul))

    TampilTabel(NimList, NilaiMahasiswa, NilaiIndeks)

menuPilihan(NimList, NilaiMahasiswa, NilaiIndeks)
