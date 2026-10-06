import csv

vards = input("Tavs vārds: ")
pilseta = input("Tava pilsēta: ")

with open("personas_rakstit.csv", "a", encoding="utf-8") as file:
    # writer = csv.writer(file)
    # writer.writerow([vards, pilseta])
    writer = csv.DictWriter(file, fieldnames=["vards", "pilseta"])
    writer.writerow({"vards": vards, "pilseta": pilseta})