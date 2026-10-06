import pandas as pd

dati = pd.read_csv("Squirrel_Data.csv")

pelekas = len(dati[dati["Primary Fur Color"] == "Gray"])
rudas = len(dati[dati["Primary Fur Color"] == "Cinnamon"])
melnas = len(dati[dati["Primary Fur Color"] == "Black"])
print("Pelēkās", pelekas)
print("Rudās", rudas)
print("Melnās", melnas)

dati_dict = {
    "krāsas": ["Ruda", "Pelēka", "Melna"],
    "skaits": [rudas, pelekas, melnas]
}

df = pd.DataFrame(dati_dict)
df.to_csv("vaveru_skaits.csv", encoding="utf-8")