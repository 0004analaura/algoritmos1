import sys

def main():
   
    valores = sys.argv[1].split(",")

   
    for valor in valores:
        try:
            float(valor)
        except ValueError:
            print("Error: los valores deben ser números.")
            return


    suma = sum(valores)

 
    promedio = suma / len(valores)


    print("Suma:", suma)
    print("Promedio:", promedio)

if __name__ == "__main__":
    main()