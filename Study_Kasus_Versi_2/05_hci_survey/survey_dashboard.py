"""Visualisasi hasil survei kepuasan sintetis."""
import pandas as pd
import matplotlib.pyplot as plt

survey = pd.DataFrame({
    "Aspek": ["Materi", "Pemateri", "Fasilitas", "Waktu", "Penyelenggaraan"],
    "Rata-rata (1-5)": [4.4, 4.6, 3.8, 3.5, 4.2],
})
print("Ringkasan survei (data contoh):")
print(survey.to_string(index=False))

ax = survey.plot(x="Aspek", y="Rata-rata (1-5)", kind="bar", legend=False, ylim=(0, 5))
ax.set_title("Ringkasan Kepuasan Peserta")
ax.set_xlabel("Aspek yang Dinilai")
ax.set_ylabel("Rata-rata Nilai")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("survey_summary.png", dpi=150)
print("\nGrafik disimpan sebagai survey_summary.png")
