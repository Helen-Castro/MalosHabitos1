
"Castro Arteaga Helen-Rojas Ortiz Franklin"
def multiplicar(a, b):
    return a * b

while True:
    try:
        primer_numero = int(input("Ingrese el primer número: "))
        segundo_numero = int(input("Ingrese el segundo número: "))
        resultado = multiplicar(primer_numero, primer_numero + segundo_numero)
        print("El resultado es:", resultado)
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
    if input("¿Desea realizar otra operación? (s/n): ").lower() != 's':
        break