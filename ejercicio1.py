def contar_letra(string, letra):
    return string.count(letra)

string = input("Ingrese un string:")
letra = input ("Ingrese una letra:")

contador = contar_letra(string, letra)
print(f"La letra' {letra} 'aparece {contador} veces en el string '{string} '.")
