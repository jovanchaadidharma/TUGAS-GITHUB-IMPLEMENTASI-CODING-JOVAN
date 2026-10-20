"""Segmentasi pelanggan sederhana berbasis aturan."""
import pandas as pd

df = pd.DataFrame([
    {"pelanggan": "P001", "transaksi": 12, "total_belanja": 1800000},
    {"pelanggan": "P002", "transaksi": 3, "total_belanja": 240000},
    {"pelanggan": "P003", "transaksi": 8, "total_belanja": 950000},
    {"pelanggan": "P004", "transaksi": 1, "total_belanja": 75000},
    {"pelanggan": "P005", "transaksi": 10, "total_belanja": 1250000},
    {"pelanggan": "P006", "transaksi": 4, "total_belanja": 320000},
])

def segment(row):
    if row["transaksi"] >= 8 and row["total_belanja"] >= 900000:
        return "Pelanggan loyal"
    if row["transaksi"] >= 4:
        return "Pelanggan berkembang"
    return "Pelanggan baru/jarang"

df["segmen"] = df.apply(segment, axis=1)
print("=== Segmentasi Pelanggan ===")
print(df.to_string(index=False))
print("\nJumlah pelanggan per segmen:")
print(df["segmen"].value_counts().to_string())
print("\nIde tindakan: loyal—program apresiasi; berkembang—promo bundling; baru/jarang—promo pengenalan.")
