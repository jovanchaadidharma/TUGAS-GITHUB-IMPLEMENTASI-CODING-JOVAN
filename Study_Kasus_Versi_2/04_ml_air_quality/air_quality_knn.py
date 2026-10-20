"""Klasifikasi edukatif kualitas udara memakai KNN."""
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Fitur sintetis: partikel halus (skor relatif) dan gas (skor relatif).
X = [
    [12, 10], [15, 12], [18, 14], [20, 18], [22, 20],
    [30, 28], [35, 32], [38, 35], [42, 40], [45, 44],
    [55, 52], [60, 58], [65, 63], [70, 68], [75, 72],
    [14, 16], [33, 36], [48, 46], [58, 61], [72, 70],
    [17, 11], [40, 37], [63, 60], [68, 75],
]
y = (["Rendah"] * 8) + (["Sedang"] * 8) + (["Tinggi"] * 8)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=11, stratify=y
)
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"Akurasi contoh: {accuracy_score(y_test, pred):.2f}")
print("Kategori untuk sensor [32, 30]:", model.predict([[32, 30]])[0])
print("Catatan: fitur dan label sintetis; bukan indeks kualitas udara resmi.")
