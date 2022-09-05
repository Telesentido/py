print("ingrese la cantidad de segundos a convertir : ")

segundos = int(input()) 

# la doble barra // toma solo la parte entera del cociente

dia = segundos // 86400

horas = (segundos % 86400) // 3600

minutos = ((segundos % 86400) % 3600) // 60

segundos = ((segundos % 86400) % 3600) % 60

print("La cantidad de dias equivales es :", dia)

print("La cantidad de horas equivales es :", horas)

print("La cantidad de minutos equivales es :", minutos)

print("La cantidad de segundos equivales es :", segundos)
