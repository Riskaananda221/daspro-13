# Visualisasi Profesi Warga

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_excel("Data_Penduduk.xlsx")
profesi_counts = data["Profesi"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(profesi_counts, labels=profesi_counts.index, autopct="1%.1f%%", startangle=140)
plt.title("Persentase Profesi Warga Desa")
plt.axis("equal")
plt.show()