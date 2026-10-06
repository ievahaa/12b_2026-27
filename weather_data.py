# No datnes nolasīt tikai temperatūras
# import csv

# with open("weather_data.csv") as file:
#     dati = csv.reader(file)
#     temperaturas = []
#     for rinda in dati:
#         if rinda[1] != "temp":
#             temperaturas.append(int(rinda[1]))
#     print(temperaturas)

import pandas

dati = pandas.read_csv("weather_data.csv")
temper = dati["temp"]

dati_dict = dati.to_dict()
print(dati_dict)

dati_list = temper.to_list()
print(dati_list)

#Aprēķināt vidējo temperatūru
print(temper.mean())

#Aprēķināt maksimālo temperatūru
print(temper.max())

#dati pa kolonām
print(temper)
print(dati.condition)

#dati pa rindām
print(dati[dati.day == "Monday"])

#kurā dienā ir max temperatūra?
print(dati[dati.temp == dati.temp.max()])

#Aprēķināt pirmdienas temperatūru Fārenheitos
#(t*9/5)+32
pirmdiena = dati[dati.day == "Monday"]
pirmd_temp = pirmdiena.temp[0]
pirmd_F = pirmd_temp * 9/5 + 32
print(pirmd_F)

#izveido dataframe kā vārdnīcu
datu_dict = {
    "skolēni": ["Ilze", "Zane", "Aleksis"],
    "atzīmes": [9, 7, 8]
}

dati = pandas.DataFrame(datu_dict)
print(dati)
dati.to_csv("jaunie_dati.csv", encoding="utf-8")