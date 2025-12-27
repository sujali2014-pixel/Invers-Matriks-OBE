import numpy as np

def input_matriks_numpy():
    print("=== INPUT MATRIKS 3x3 ===")
    matriks = []
    for i in range(3):
        row = []
        print(f"--- Baris ke-{i+1} ---")
        for j in range(3):
            while True:
                try:
                    val = float(input(f"Elemen [{i+1},{j+1}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Input angka saja.")
        matriks.append(row)
    return np.array(matriks, dtype=float)

def cetak_langkah(aug_matriks, langkah, deskripsi):
    """Visualisasi Matriks Augmented menggunakan NumPy"""
    print(f"\n--- Langkah {langkah}: {deskripsi} ---")
    
    # Mengambil bagian kiri (A) dan kanan (I)
    # NumPy slicing sangat mudah: [semua baris, kolom 0-3]
    kiri = aug_matriks[:, :3]
    kanan = aug_matriks[:, 3:]
    
    print("-" * 50)
    for k, i in zip(kiri, kanan):
        # Format string agar rapi
        str_kiri = "  ".join([f"{x:6.2f}" for x in k])
        str_kanan = "  ".join([f"{x:6.2f}" for x in i])
        print(f"| {str_kiri}  |  {str_kanan} |")
    print("-" * 50)

def invers_obe_numpy_step(matriks_asal):
    n = len(matriks_asal)
    
    # 1. AUGMENTASI
    # np.hstack menempelkan matriks secara horizontal (kiri-kanan)
    # Ini jauh lebih ringkas daripada loop append manual
    identitas = np.eye(n)
    aug = np.hstack((matriks_asal, identitas))
    
    cetak_langkah(aug, 0, "Matriks Awal [ A | I ]")
    step = 1

    # 2. ELIMINASI GAUSS-JORDAN
    for i in range(n):
        # --- A. Pivot & Swap ---
        pivot = aug[i, i]
        
        if np.isclose(pivot, 0): # Cek jika 0 (aman untuk float)
            # Cari baris di bawahnya untuk ditukar
            for k in range(i + 1, n):
                if not np.isclose(aug[k, i], 0):
                    # Fitur NumPy: Tukar baris cuma butuh 1 baris kode!
                    aug[[i, k]] = aug[[k, i]] 
                    pivot = aug[i, i]
                    cetak_langkah(aug, step, f"Tukar Baris {i+1} & {k+1}")
                    step += 1
                    break
            else:
                return None # Singular

        # --- B. Normalisasi (Membuat 1 Utama) ---
        # KEAJAIBAN NUMPY: Kita bisa membagi SELURUH baris tanpa loop 'for j in...'
        aug[i] = aug[i] / pivot
        
        cetak_langkah(aug, step, f"Baris {i+1} dibagi {pivot:.2f}")
        step += 1

        # --- C. Eliminasi (Membuat 0) ---
        for k in range(n):
            if k != i:
                faktor = aug[k, i]
                # KEAJAIBAN NUMPY: Operasi pengurangan seluruh baris sekaligus
                # Rumus: R_k = R_k - (faktor * R_i)
                aug[k] = aug[k] - (faktor * aug[i])
                
                # Kita cetak hanya jika ada perubahan signifikan
                if not np.isclose(faktor, 0):
                    cetak_langkah(aug, step, f"Baris {k+1} - ({faktor:.2f} * Baris {i+1})")
                    step += 1

    # 3. AMBIL HASIL
    return aug[:, n:] # Ambil kolom ke-3 sampai akhir

# --- JALANKAN ---
if __name__ == "__main__":
    np.set_printoptions(suppress=True) # Agar output array bersih (0.00 bukan 1e-16)
    
    user_mat = input_matriks_numpy()
    hasil = invers_obe_numpy_step(user_mat)

    if hasil is not None:
        print("\n=== HASIL AKHIR INVERS ===")
        print(hasil)
    else:
        print("\n[!] Matriks Singular (Tidak punya invers)")git 