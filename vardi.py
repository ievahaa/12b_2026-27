# vards = input("Kā tevi sauc? ")

# # file = open("vardi.txt", "w", encoding="utf-8")
# # file.write(vards)
# # file.close()

# with open("vardi.txt", "a", encoding="utf-8") as file:
#     file.write(f"{vards}\n")

with open("vardi.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()


for rinda in rindas:
    print("sveiki,",rinda.rstrip())