# Uzraksti programmu, kas pajautā skolēna vārdu un iegūto punktu skaitu (0–100).
# • Izvadi skolēna vārdu un punktus vienā teikumā.
# • Ja punkti ir vismaz 80, izvadi “Lieliski!”, ja vismaz 50 — “Ieskaitīts!”, citādi — “Jāturpina trenēties!”.
# • Pārbaudi programmu ar vērtībām 49, 50 un 80.

# vards = input("Ieraksti vārdu: ")
# punkti = int(input("Ieraksti punktus: "))
# if punkti >= 80:
#     print(f"{vards} ieguva {punkti} punktus - lieliski!")
# elif punkti >= 50:
#     print(f"{vards} ieguva {punkti} punktus - ieskaitīts!")
# else:
#     print(f"{vards} ieguva {punkti} punktus - jāturpina trenēties!")


# • Izveido funkciju siltas_dienas(temperaturas), kas ar filter un lambda atlasa temperatūras, kas ir vismaz 20 °C.
# • Funkcijai jāatgriež saraksts, nevis tas jāizdrukā.
# • Izsauc funkciju un izdrukā rezultātu un silto dienu skaitu.

temperaturas = [18, 21, 16, 23, 25, 19]

def siltas_dienas(temperaturas):
    return list(filter(lambda t: t >= 20, temperaturas))

siltas = siltas_dienas(temperaturas)
print(siltas)
print(f"Silto dienu skaits: {len(siltas)}")


# Izveido funkciju gala_cena(cena, atlaide), kas aprēķina cenu pēc atlaides. Atlaide ir % no cenas.
# • Ja cena ir negatīva vai atlaide nav intervālā no 0 līdz 100, izsauc ValueError.
# • Citādi atgriez rezultātu, noapaļotu līdz 2 zīmēm aiz komata.
# • Uzraksti vismaz divus assert testus: vienu korektam aprēķinam un vienu robežgadījumam.

def gala_cena(cena, atlaide):
    if cena < 0 or not 0 <= atlaide <= 100:
        raise ValueError("Nederīga cena vai atlaide")
    return round(cena * (1 - atlaide / 100), 2)

print(gala_cena(20, 5))

assert gala_cena(100, 20) == 80.00
assert gala_cena(50, 0) == 50.00