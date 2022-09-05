Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lista = [1, 3, 5, 10, 4]
>>> lista.append(8)
>>> lista
[1, 3, 5, 10, 4, 8]
>>> lista.clear()
>>> lista
[]
>>> lista = [1, 3, 5, 10, 4]
>>> lista
[1, 3, 5, 10, 4]
>>> id(lista)
36681688
>>> lista2 = [1, 3, 5, 10, 4]
>>> lista2
[1, 3, 5, 10, 4]
>>> id(lista2)
36681608
>>> lista3=lista.copy()
>>> lista3
[1, 3, 5, 10, 4]
>>> lista.append(5)
>>> lista
[1, 3, 5, 10, 4, 5]
>>> lista.count(5)
2
>>> lista.append(lista2)
>>> lista
[1, 3, 5, 10, 4, 5, [1, 3, 5, 10, 4]]
>>> lista.r
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lista.r
AttributeError: 'list' object has no attribute 'r'
>>> lista.remove(lista2)
>>> lista
[1, 3, 5, 10, 4, 5]
>>> lista.extend(lista2)
>>> lista
[1, 3, 5, 10, 4, 5, 1, 3, 5, 10, 4]
>>> lista.index(5)
2
>>> lista.index(0)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lista.index(0)
ValueError: 0 is not in list
>>> lista.index(1)
0
>>> lista.index(3)
1
>>> lista.index(1)
0
>>>  lista.index(1, 2)
 
SyntaxError: unexpected indent
>>>  lista.index(1, 1)
 
SyntaxError: unexpected indent
>>>  lista.index(1, 3)
 
SyntaxError: unexpected indent
>>> lista.index(1)
0
>>> lista.index(1,1)
6
>>> lista
[1, 3, 5, 10, 4, 5, 1, 3, 5, 10, 4]
>>> lista.insert(0,2)
>>> lista
[2, 1, 3, 5, 10, 4, 5, 1, 3, 5, 10, 4]
>>> lista.pop(0)
2
>>> lista
[1, 3, 5, 10, 4, 5, 1, 3, 5, 10, 4]
>>> lista.insert(1,2)
>>> lista
[1, 2, 3, 5, 10, 4, 5, 1, 3, 5, 10, 4]
>>> lista.remove (19)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    lista.remove (19)
ValueError: list.remove(x): x not in list
>>> lista.remove (10)
>>> lista
[1, 2, 3, 5, 4, 5, 1, 3, 5, 10, 4]
>>> lista.remove (10)
>>> lista3
[1, 3, 5, 10, 4]
.
>>> lista
[1, 2, 3, 5, 4, 5, 1, 3, 5, 4]
>>> lista.reverse()
>>> lista
[4, 5, 3, 1, 5, 4, 5, 3, 2, 1]
>>> lista = ["rio", "agua","pez", sol"]
	 
SyntaxError: EOL while scanning string literal
>>> lista = ["rio", "agua","pez", "sol"]
>>> lista
['rio', 'agua', 'pez', 'sol']
>>> list.sort()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    list.sort()
TypeError: descriptor 'sort' of 'list' object needs an argument
>>> lista.sort()
>>> lista
['agua', 'pez', 'rio', 'sol']
>>> lista.sort(key=len)
>>> ista
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ista
NameError: name 'ista' is not defined
>>> lista
['pez', 'rio', 'sol', 'agua']
>>> lista.sort(key=sort)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lista.sort(key=sort)
NameError: name 'sort' is not defined
>>> lista
['pez', 'rio', 'sol', 'agua']
>>> lista.sort()
>>> lista
['agua', 'pez', 'rio', 'sol']
>>> for lista in lista
SyntaxError: invalid syntax
>>> for lista in lista:
	print(lista)

	
agua
pez
rio
sol
>>> for lista in lista:
	print(lista.rever())

	
Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    print(lista.rever())
AttributeError: 'str' object has no attribute 'rever'
>>> for lista in lista:
	print(lista.reverse())

	
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    print(lista.reverse())
AttributeError: 'str' object has no attribute 'reverse'
>>> for lista in lista:
	print (lista.sort)

	
Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    print (lista.sort)
AttributeError: 'str' object has no attribute 'sort'
>>> lista
's'
>>> lista = ["rio", "agua","pez", "sol"]
>>> lista
['rio', 'agua', 'pez', 'sol']
>>>  dueno = [28957346, "Juan,  Perez", 4789689, "Belgrano 101"]
 
SyntaxError: unexpected indent
>>> dueno = [28957346, "Juan,  Perez", 4789689, "Belgrano 101"]
>>> dueno
[28957346, 'Juan,  Perez', 4789689, 'Belgrano 101']
>>> lista
['rio', 'agua', 'pez', 'sol']
>>> for lista in lista:
	print (lista)

	
rio
agua
pez
sol
>>> for lista in lista:
	print (lista.reverse(true))

	
Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    print (lista.reverse(true))
AttributeError: 'str' object has no attribute 'reverse'
>>> for lista in lista:
	print (lista.reverse = true)
	
SyntaxError: keyword can't be an expression
>>> for lista in lista:
	print (lista.reverse)

	
Traceback (most recent call last):
  File "<pyshell#89>", line 2, in <module>
    print (lista.reverse)
AttributeError: 'str' object has no attribute 'reverse'
>>> for lista in lista:
	print (lista -1)

	
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    print (lista -1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>>  for lista in lista:
	print (lista (-1))
	
SyntaxError: unexpected indent
>>> for lista in lista:
	print (lista (-1))

	
Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    print (lista (-1))
TypeError: 'str' object is not callable
>>> lista
's'
>>> listas
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    listas
NameError: name 'listas' is not defined
>>> lista
's'
>>> s
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> lista = ["rio", "agua","pez", sol"]
	 
SyntaxError: EOL while scanning string literal
>>> lista = ["rio", "agua","pez", "sol"]
>>> lista
['rio', 'agua', 'pez', 'sol']
>>> for lista in lista:
	print (lista.sort)

	
Traceback (most recent call last):
  File "<pyshell#105>", line 2, in <module>
    print (lista.sort)
AttributeError: 'str' object has no attribute 'sort'
>>> lista
'rio'
>>> lista = ["rio", "agua","pez", "sol"]
>>> lista
['rio', 'agua', 'pez', 'sol']
>>> lista.sort()
>>> 
>>> lista
['agua', 'pez', 'rio', 'sol']
>>> lista = ["rio", "agua","pez", "sol"]
>>> lista
['rio', 'agua', 'pez', 'sol']
>>> for lista in lista:
	print (lista.sort(""))

	
Traceback (most recent call last):
  File "<pyshell#122>", line 2, in <module>
    print (lista.sort(""))
AttributeError: 'str' object has no attribute 'sort'
>>> # 10) Crear una lista denominada “Clientes” con los nombres de los diferentes  dueños de perros.

          Juan,  Mario,  Ariel,  Josefina,  Marianella.

Ordenarla alfabéticamente y mostrarla por pantalla.
SyntaxError: unexpected indent
>>> clientes = ["Juan",  Mario,  Ariel,  Josefina,  Marianella]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    clientes = ["Juan",  Mario,  Ariel,  Josefina,  Marianella]
NameError: name 'Mario' is not defined
2
>>> clientes = ["Juan",  "Mario", "Ariel",  "Josefina",  "Marianella"]
>>> print (clientes.sort())
None
>>> clientes
['Ariel', 'Josefina', 'Juan', 'Marianella', 'Mario']
>>> print (clientes)
['Ariel', 'Josefina', 'Juan', 'Marianella', 'Mario']
>>> # clientes = ["Juan",  "Mario", "Ariel",  "Josefina",  "Marianella"]
>>> # clientes = ["Juan",  "Mario", "Ariel",  "Josefina",  "Marianella"]
>>> clientes = ["Juan",  "Mario", "Ariel",  "Josefina",  "Marianella"]
SyntaxError: invalid syntax
>>> clientes = ["Juan",  "Mario", "Ariel",  "Josefina",  "Marianella"]
