inputfile_one = "INN.csv"
data = []
seek_data = input("Введите номер или название объекта про которого хотите найти информацию: ").strip()
arr = []
with (open(inputfile_one, "r", encoding="utf-8") as file):
    for l in file:
        row = l.strip().split(";")
        arr.append(row)
for i in arr:
    if seek_data == i[2]:
        ind = i[0]
        print(f"{ind}")
for i in arr:
    if i[1] == ind:
        print(f"Вы ввели номер этого объекта: {i[3]}")
