# calculadora con las 4 operaciones aritmeticas 


print('''\t<:MENU:>
(S,s) Suma
(R,s) resta
(M,n) Multiplicacion
(D,d) Divion
''')

print('Agrega los numeros para efectuar la operacion')


numero1 = int(input('Numero a: '))
numero2 = int(input('Numero b: '))

print('Elija la Opcion')
opcion = input('Operacion Aritmetica:')

if opcion=="S" or opcion=="s":
    suma = numero1 + numero2
    print(f'El resultado es: {suma}')
elif opcion=="R" or opcion=="r":
    resta = numero1 - numero2
    print(f'El resultado es: {resta}')
elif opcion=="M" or opcion=="m":
    Multiplicacion = numero1 * numero2
    print(f'El resultado es: {Multiplicacion}')
elif opcion=="D" or opcion=="d":
    division = numero1 / numero2
    print(f'El resultado es: {division}')
else:
    print("esa opcion no existe")