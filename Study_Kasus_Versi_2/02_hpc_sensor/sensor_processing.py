"""Demo pemrosesan data sensor serial dan paralel."""
from multiprocessing import Pool
from time import perf_counter
import random

def partial_stats(values):
    return sum(values), len(values)

def split_data(data, parts):
    size = max(1, len(data) // parts)
    return [data[i:i + size] for i in range(0, len(data), size)]

if __name__ == "__main__":
    random.seed(21)
    sensor_data = [random.uniform(18.0, 35.0) for _ in range(600_000)]

    start = perf_counter()
    serial_sum, serial_count = partial_stats(sensor_data)
    serial_time = perf_counter() - start

    chunks = split_data(sensor_data, 4)
    start = perf_counter()
    with Pool(processes=4) as pool:
        partial = pool.map(partial_stats, chunks)
    parallel_sum = sum(item[0] for item in partial)
    parallel_count = sum(item[1] for item in partial)
    parallel_time = perf_counter() - start

    print(f"Jumlah data sensor : {serial_count:,}")
    print(f"Rata-rata serial   : {serial_sum / serial_count:.3f}")
    print(f"Rata-rata paralel  : {parallel_sum / parallel_count:.3f}")
    print(f"Waktu serial       : {serial_time:.4f} detik")
    print(f"Waktu paralel      : {parallel_time:.4f} detik")
    print("Hasil konsisten    :", abs(serial_sum - parallel_sum) < 1e-6)
