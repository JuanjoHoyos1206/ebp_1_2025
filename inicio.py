print("Inicio del programa")

numero = int(input("ingrese un numero entre 1 y 20: "))
if numero in (2):
    print("su numero es par y primo") 
elif numero in (4, 6, 8, 10, 12, 14, 16, 18, 20):
    print("su numero es par")
elif numero in (2, 3, 5, 7, 11, 13, 17, 19):
    print("Su numero es primo", "y es impar")
elif numero in (9, 15):
    print("su numero es impar")
else:print("su numero no esta en el rango")

print("fin del programa")