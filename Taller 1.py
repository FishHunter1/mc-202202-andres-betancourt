a,b,c = set(), set(), set()

n = int(input("ingrese el cardinal del conjunto A: "))
for x in range(0, n):
    elem = int(input("Ingrese un elemento del conjunto A: "))
    a.add(elem)
print("El conjunto A contiene =",a)

n = int(input("ningrese el cardinal del conjunto B: "))
for x in range(0, n):
    elem = int(input("Ingresa un elemento del conjunto B: "))
    b.add(elem)
print("El conjunto A =",a,"\nEl conjunto B =",b)

menu=["union","interseccion","diferencia","diferencia simetrica","salir"]
isAddprueba=True
isActive=True
opcion=0
print("¿Qué operación deseas realizar entre los conjuntos A y B para obtener el conjunto C?")

while isActive:
    isAddprueba=True
    for i in range(len(menu)):
        print(f"{i+1}-{menu[i]}")
    try:
        opcion=int(input(":)_ "))
    except:
        print("Error en opcion")
        opcion=0
    else:
        if opcion == 1:
            for x in a:
                c.add(x)
                print("\nA =",a,"\nB =",b,"\n\nA ∪ B = C \nC =",c,"\n|C| =",len(c))
        elif opcion == 2:
                for x in a:
                    if x in b:
                        c.add(x)
                        print("\nA =",a,"\nB =",b,"\n\nA ∩ B = C \nC =",c,"\n|C| =",len(c))
        elif opcion == 3:
                for x in a:
                    if x not in b:
                        c.add(x)
                        print("\nA =",a,"\nB =",b,"\n\nA - B = C \nC =",c,"\n|C| =",len(c))
        elif opcion == 4:
            for x in b:
                if x not in a:
                    c.add(x)
                    print("\nA =",a,"\nB =",b,"\n\nB - A = C \nC =",c,"\n|C| =",len(c))
        elif n == 5:
            for x in a:
                if x not in b:
                    c.add(x)
            for x in b:
                if x not in a:
                    c.add(x)
                    print("\nA =",a,"\nB =",b,"\n\nA △ B = C \nC =",c,"\n|C| =",len(c))