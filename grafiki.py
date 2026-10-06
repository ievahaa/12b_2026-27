import matplotlib.pyplot as plt

fig = plt.figure() #nodefinē pamata laukumu

#y = 2x
# x = [-3, -2, -1, 0, 1, 2, 3]
# y = [-6, -4, -2, 0, 2, 4, 6]

x = list(range(-10, 11))
y = [n**2 for n in x]

plt.plot(x, y, color="green", linewidth=10)
plt.title('Funkcijas y = x**2 grafiks')
plt.xlabel('x ass')
plt.ylabel('y ass')
plt.grid()

plt.show()