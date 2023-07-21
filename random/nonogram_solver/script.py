import sys
import mTest

with open("data" + str(sys.argv[1]) + ".txt", "w") as file:
    file.write("")

# Cambiar linea 64 de mTest
for i in range(100):
    exec(open(".\mTest.py").read())

with open("data" + str(sys.argv[1]) + ".txt") as f:
    lines = f.readlines()

contGana = lines.count("True\n")
contPierde = lines.count("False\n")

# print(lines)

print("Gana: ", contGana)
print("Pierde: ", contPierde)
total = contGana + contPierde
promedio = contGana / total
print("Promedio: ", promedio)
