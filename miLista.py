# Ejemplo de uso de listas
Misnovias= ["Vale", "Valeria", "Val"]
misNumeros= [666,123,456]
print(Misnovias) 
print (misNumeros)
print ("--accediendo a los elementos de la lista--")
print(Misnovias[1]) 

if "Vale" in Misnovias:
 print("si, 'vale♥' si es mi novia")
else:
 print("no esta en la lista de novias")
print ("numero de novia")

NMisnovias=len(Misnovias)
print (f"numero de novia {NMisnovias}")


print ("Ciclo for en lista")
posicion=0

for corazon in Misnovias:
    print( corazon)

