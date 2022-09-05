lado1 = float(input("ingrese el primer lado : "))
lado2 = float(input("ingrese el segundo lado : "))
lado3 = float(input("ingrese el tercer lado : "))

perimetro = lado1 + lado2 + lado3

Sp = perimetro / 2

superficie = (Sp*(Sp-lado1)*(Sp-lado2)*(Sp-lado3))**0.5

print("El valor del perimetro es :", perimetro)

print("El valor de la superficie es :", superficie)