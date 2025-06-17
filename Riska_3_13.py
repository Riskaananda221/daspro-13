# 3. Distribusi Penghasilan

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Data_Penduduk.xlsx")
data.columns = data.columns.str.strip()

def kategori_penghasilan(nilai):
    if nilai < 1000000:
        return "Sangat Rendah"
    elif nilai < 2500000:
        return "Rendah"
    elif nilai < 5000000:
        return "Menengah"
    else:
        return"Tinggi"
    
    data["Kategori_Penghasilan"] = data["Penghasilan_Per_Bulan"].apply(Kategori_Penghasilan)
    penghasilan_counts = data["Kategori_Penghasilan"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(penghasilan_counts, labels=penghasilan_counts.index, autopct="%1.1f%%", startangle=90, colors=["#FF9999", "#FFCC99" "#99CCFF", "#66FF66"])
    plt.title("Distribusi Penghasilan Warga Desa Cibodas")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()