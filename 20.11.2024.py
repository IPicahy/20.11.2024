inputfile_one = "INN.csv"
data = []
seek_data = input("Введите номер или название объекта про которого хотите найти информацию: ").strip()

with (open(inputfile_one, "r", encoding="utf-8") as file):
    for l in file:
        row = l.strip().split(";")

        for i in row[2]:
            if seek_data in i and not i == "":
                ind = row[0]
                print(f"Вы ввели название этого объекта: {row[0]}-{row[1]}-{row[2]} ({row[3]})")

        if row[2] == seek_data:
            ind = row[0]
            print(f"Вы ввели номер этого объекта: {row[0]}-{row[1]}-{row[2]} ({row[3]})")

with (open(inputfile_one, "r", encoding="utf-8") as file):
    for l in file:
        row = l.strip().split(";")
        if ind==row[1]:
            print(f"{row[0]}-{row[1]}-{row[2]} ({row[3]})")

