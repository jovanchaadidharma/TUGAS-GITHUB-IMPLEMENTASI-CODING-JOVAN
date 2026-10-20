"""Prioritas pemeriksaan alert perubahan lahan dengan data sintetis."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Fitur: perubahan vegetasi (0-1), kedekatan jalan (0-1), luas relatif (0-1).
X = [
    [0.10, 0.20, 0.10], [0.20, 0.30, 0.15], [0.25, 0.10, 0.20],
    [0.35, 0.25, 0.30], [0.45, 0.40, 0.40], [0.50, 0.50, 0.35],
    [0.60, 0.60, 0.55], [0.70, 0.65, 0.70], [0.80, 0.75, 0.80],
    [0.90, 0.85, 0.90], [0.15, 0.10, 0.10], [0.40, 0.35, 0.45],
    [0.55, 0.45, 0.60], [0.65, 0.80, 0.65], [0.75, 0.55, 0.75],
    [0.30, 0.20, 0.35], [0.85, 0.90, 0.85], [0.48, 0.60, 0.45],
]
y = [
    "Rendah", "Rendah", "Rendah", "Rendah", "Sedang", "Sedang",
    "Sedang", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Sedang",
    "Sedang", "Tinggi", "Tinggi", "Rendah", "Tinggi", "Sedang",
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=19, stratify=y
)
model = RandomForestClassifier(n_estimators=100, random_state=19)
model.fit(X_train, y_train)
print("Laporan evaluasi pada data contoh:")
print(classification_report(y_test, model.predict(X_test), zero_division=0))

alert = [[0.72, 0.68, 0.74]]
print("Prioritas untuk alert sintetis:", model.predict(alert)[0])
print("Periksa hasil dengan data citra dan verifikasi manusia sebelum mengambil tindakan.")
