# piezime = input("Ievadi piezīmi: ") 

# with open("piezime.txt", "w") as fails: 
#     fails.write(piezime) 

# with open("piezime.txt", "r") as fails: 
#     teksts = fails.read() 

# print("Saglabātā piezīme:") 
# print(teksts) 

# ideja = input("Ievadi ideju: ") 

# with open("idejas.txt", "a") as fails: 
#     fails.write(ideja + "\n") 

# print("\nSaglabātās idejas:") 

# with open("idejas.txt", "r") as fails: 
#     for rinda in fails: 
#         print(rinda.rstrip())


# gramatas = [] 

# with open("gramatas.txt", "r", encoding="utf-8") as fails: 
#     for rinda in fails: 
#         gramatas.append(rinda.rstrip()) 

# virziens = input("Izvēlies kārtošanu (A-Z vai Z-A): ") 

# if virziens == "Z-A": 
#     gramatas = sorted(gramatas, reverse=True) 
# else: 
#     gramatas = sorted(gramatas) 

# for gramata in gramatas: 
#     print(gramata)


mekletais = input("Ievadi skolēna vārdu: ") 

atrasts = False 

with open("skoleni.txt", "r", encoding="utf-8") as fails: 
    for rinda in fails: 
        vards = rinda.rstrip() 
        if vards.lower() == mekletais.lower(): 
            atrasts = True 

if atrasts: 
    print(mekletais, "ir sarakstā.") 
else: 
    print(mekletais, "nav sarakstā.")