# with open("teksts.txt", mode="a", encoding="utf-8") as file:
#     file.write("\nNākamais teksts")

file = open("teksts.txt", mode="r", encoding="utf-8")
# rindas = file.readlines()
# print(rindas)
for rinda in file:
    print(rinda.rstrip())
file.close()

#uzdevums - izveidot datni ar 4 rindu dzejoli, nolasīt to ar Python