# Saskaita un izdrukā pilnā teikumā cik jaundzimušo dotajā laika periodā ir zēni un cik meitenes,
# Izdrukā, kurā periodā ir dzimušas visvairāk meitenes,
# Izdrukā, kurā periodā ir dzimuši vaisvairāk zēni,
# Izdrukā kāds ir vidējais jaundzimušo skaits mēnesī.

import pandas

dati = pandas.read_csv('dzimusie.csv', encoding="utf-8")
viriesi = dati["Viriesi"]
sievietes = dati["Sievietes"]
vir_sk = viriesi.sum()
siev_sk = sievietes.sum()
print(f"Dotajā laika periodā ir dzimuši {vir_sk} zēni un {siev_sk} meitenes.")

max_siev = max(sievietes)
siev_menesis = dati[dati["Sievietes"] == max_siev]
print(siev_menesis[["Laika periods"][0]])
max_vir = max(viriesi)
vir_menesis = dati[dati["Viriesi"] == max_vir]
print(vir_menesis[["Laika periods"][0]])

rindu_sk = len(dati["Sievietes"])
videjais = (vir_sk + siev_sk)/rindu_sk
print(round(videjais))