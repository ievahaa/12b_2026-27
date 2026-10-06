import csv

pers = []

with open("personas.csv", encoding="utf-8") as file:
    # reader = csv.reader(file)
    # for vards, pilseta in reader:
    #     pers.append({"vards": vards, "pilseta": pilseta})
    reader = csv.DictReader(file)
    for rinda in reader:
        pers.append({"vards": rinda["vards"], "pilseta": rinda["pilseta"]})

def pers_vards(persona):
    return persona["vards"]

def pers_pilseta(persona):
    return persona["pilseta"]

for i in sorted(pers, key=pers_vards, reverse=False):
    print(f"{i['vards']} ir no pilsētas {i['pilseta']}") 

