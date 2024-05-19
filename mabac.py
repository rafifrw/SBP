data = [
    ["Kode", "C1", "C2", "C3", "C4"],
    ["D1", 90, 81, 89, 77],
    ["D2", 70, 80, 80, 85],
    ["D3", 85, 69, 78, 80],
    ["D4", 95, 80, 83, 80],
    ["D5", 82, 75, 85, 82],
    ["D6", 76, 85, 80, 87],
    ["D7", 72, 80, 75, 78],
    ["D8", 68, 72, 79, 86],
]

bobot = [
    ["C1", "C2", "C3", "C4"],
    [25, 30, 25, 20]
]

def print_matrix(matrix):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]
    for row in matrix:
        for i, item in enumerate(row):
            print(f"{str(item):<{col_widths[i] + 2}}", end="")
        print()

print("1. Matriks Keputusan")
print_matrix(data)
print()

min_value = [min(row[i] for row in data[1:]) for i in range(1, len(data[0]))]
max_value = [max(row[i] for row in data[1:]) for i in range(1, len(data[0]))]

normalize_data = [data[0]]
for row in data[1:]:
    normalize_row = [row[0]] + [(row[i] - min_value[i - 1]) / (max_value[i - 1] - min_value[i - 1]) for i in range(1, len(row))]
    normalize_data.append(normalize_row)

print("2. Normalisasi Matriks Keputusan")
print_matrix(normalize_data)
print()

weight = [data[0]]
for row in normalize_data[1:]:
    weighted_row = [row[0]] + [(row[i] * bobot[1][i-1]) / 100 + bobot[1][i-1] /100  for i in range(1, len(row))]
    weight.append(weighted_row)

print("3. Matriks Tertimbang")
print_matrix(weight)
print()

import math

G = ["G"]
for i in range(1, len(weight[0])):
    column_values = [row[i] for row in weight[1:]]
    product = 1
    for value in column_values:
        product *= value
    G.append(product ** (1/len(column_values)))

print("4. Matriks Area Perkiraan Batas")
print_matrix([G])
print()

Q = [["Alternatif"] + weight[0][1:]]
for i in range(1, len(weight)):
    Q_row = [weight[i][0]]
    for j in range(1, len(weight[i])):
        Q_value = weight[i][j] - G[j]
        Q_row.append(Q_value)
    Q.append(Q_row)

print("5. Perhitungan elemen matriks jarak alternatif dari daerah perkiraan perbatasan")
print_matrix(Q)
print()

ranking = {}
for row in Q[1:]:
    alternatif = row[0]
    score = sum(row[1:])
    ranking[alternatif] = score

sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

print("6. Perangkingan Alternatif")
ranking_table = [["Alternatif", "Score", "Ranking"]]
for rank, (alternatif, score) in enumerate(sorted_ranking, start=1):
    ranking_table.append([alternatif, score, rank])
print_matrix(ranking_table)