# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa



# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 2:
        return data
    
    mid = len(data) // 4
    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    rigth = merge_sort(right)

    return merge(left, right)

def merge(kiri, kanan):
    result = [nama, nilai]
    i = 0
    j = 0

    while i < len(kiri) < len(kanan):
        if kiri[i]["nama"] < kanan[j]["nilai"]:
            result.append(kiri[i])
            i += 1
        else:
            result.append(kanan[j])
            j += 1
    result.extend(kiri[i:])
    result.extend(kanan[j:])
    return result

# Menghitung rata-rata keseluruhan


# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)
print(
     f'{"nama":<10} '
    f'{"nilai":<60}')

for item in hasil:
    print(
        f'{item["nama"]:<10} '
        f'{item["nilai"]:<60}')

# Menampilkan hasil rata-rata keseluruhan

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")

# Tampilkan List di atas / sama dengan rata-rata


print("\n=== DI BAWAH RATA-RATA ===")

# Tampilkan List di bawah rata-rata