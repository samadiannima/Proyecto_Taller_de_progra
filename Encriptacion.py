
A = "hola" # cadena rotable
B = "chao" # cadena fija

a = list(A)

def rotate(li, x):
  return li[-x % len(li):] + li[:-x % len(li)] #rotacion de la segunda cadena.

Z = rotate(a,55) 
StrZ = "".join(Z) # Esto me genera la cadena(str) con la rotacion de caracteres ya incluido.
                  #Ejemplo "Rotacion de 55 en "hola" es "olah""

B = "chao"         #Se remplaza la cadena original por la cadena con la rotacion incluida, asi cifrando.
print(B.replace("chao", "olah"))
 
 

 
