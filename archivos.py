# cook your dish here
cantidad_instrucciones = int(input())
directorio_raiz = "Mark"
diccionario_directorios = {}
diccionario_directorios[directorio_raiz] = {}
ruta_actual = "/Mark"
 
# imprimimos la estructura de todas los subdirectorios
def imprimir(directorio_padre, directorios, nivel):
  print(directorio_padre+":")
  for directorio_hijo in directorios:
    print("--"*(nivel+1),end="")
    imprimir(directorio_hijo, directorios[directorio_hijo], nivel+1)
 
 
def insertar(ruta, nuevo_directorio):
  # Convertimos un string a un arreglo de directorios
  # Ejemplo: "/Mark/videos/perros" -> ["Mark", "videos", "perros"]
  directorios = ruta.split("/")[1:]
  diccionario_actual = diccionario_directorios
  for directorio in directorios:
    diccionario_actual = diccionario_actual[directorio]
 
  diccionario_actual[nuevo_directorio] = {}
 
 
for _ in range(cantidad_instrucciones):
  instruccion, argumento = input().split(" ")
 
  if instruccion == "cd":
    # se procesa instruccion cd
    if argumento == "..":
      # borramos el ultimo directorio, ejemplo: /Mark/videos/perros -> /Mark/videos
      ruta_actual = "/".join(ruta_actual.split("/")[:-1])
    else:
      ruta_actual = ruta_actual + "/" + argumento
  else:
    # se procesa instruccion mkdir
    insertar(ruta_actual, argumento)
 
imprimir("Mark", diccionario_directorios["Mark"], 0)