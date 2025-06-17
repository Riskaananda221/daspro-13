# 2. Perbandingan Pendidikan dan jenis kelamin 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("Data_Penduduk.xlsx")
gruoped = data.groupby(["Pendidikan_Terakhir", "Jenis_Kelamin"]).size().unstack(fill_value=0)
gruoped.plot(kind="bar", figsize=(10, 6))
plt.title("Perbandingan Pendidikan Terakhir dan Jenis Kelamin Warga")
plt.xlabel("Pendidikan Terakhir")
plt.ylabel("JUmlah Warga")
plt.xticks(rotation =45)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(title="Jenis Kelamin")
plt.tight_layout()
plt.show()