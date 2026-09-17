a = open("siege_log.txt").readlines()[2:]

for i in a:
    if i == "\n":
        continue

    if "[" in i:
        i = i[i.find("[") :]

    b = i.split("|")

    if len(b) != 4:
        print("Ошибка: некорректное колличество полей")
        continue

    if "[[" in b[0]:
        b[0] = b[0].replace("[[", "[", 1).replace("]]", "]", 1)

    if "[" not in b[0]:
        guild = "not found"
        name = b[0].strip()
        base_damage, condition, buffs = (
            b[1].strip().replace(",", ".").replace(" ", ""),
            b[2].strip(),
            b[3].strip(),
        )
    else:
        guild = b[0][1 : b[0].find("]")].upper()
        name = b[0][b[0].find("]") + 1 :].strip()
        base_damage, condition, buffs = (
            b[1].strip().replace(",", ".").replace(" ", ""),
            b[2].strip(),
            b[3].strip(),
        )

    if condition == "Active" or condition == "active":
        condition = 1.5
    else:
        condition = 0.5

    if buffs == "":
        buffs = 0

    if buffs == "N/A":
        print("Ошибка: колличество баффов не указано")
        continue

    if float(buffs) < 0:
        print("Ошибка: отрицательное колличество баффов")
        continue

    if float(base_damage) < 0:
        print("Ошибка: отрицательный урон")
        continue

    if base_damage == "inf":
        print("Ошибка: бесконечный урон")
        continue

    if guild == "":
        guild = "not found"

    damage = round(float(base_damage) * condition * (1 + 0.15 * float(buffs)), 2)
    print(f"Игрок {name} из гильдии {guild} нанес {damage} по воротам.")
