pers = []

# with open("personas.csv", encoding="utf-8") as file:
#     for rinda in file:
#         vards, pilseta = rinda.rstrip().split(",")
#         # print(f"{vards} ir no pilsētas {pilseta}")
#         pers.append(f"{vards} ir no pilsētas {pilseta}")

# for persona in sorted(pers):
#     print(persona)

with open("personas.csv", encoding="utf-8") as file:
    for rinda in file:
        vards, pilseta = rinda.rstrip().split(",")
        # persona = {}
        # persona["vards"] = vards
        # persona["pilseta"] = pilseta
        persona = {"vards":vards, "pilseta":pilseta}
        pers.append(persona)

def pers_vards(persona):
    return persona["vards"]

def pers_pilseta(persona):
    return persona["pilseta"]

for i in sorted(pers, key=pers_pilseta, reverse=False):
    print(f"{i['vards']} ir no pilsētas {i['pilseta']}") 