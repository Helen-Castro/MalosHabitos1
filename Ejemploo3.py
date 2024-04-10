"Castro Arteaga Helen-Rojas Ortiz Franklin"
def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def obtener_valor(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace('.', '', 1).isdigit():  # Verifica si el valor ingresado es un número
            return float(valor)
        else:
            print("Error: Ingrese un número válido.")

def main():
    b_rectangulo = obtener_valor("Ingrese la base del rectángulo: ")
    h_rectangulo = obtener_valor("Ingrese la altura del rectángulo: ")
    area_rectangulo = calcular_area_rectangulo(b_rectangulo, h_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    print()  # Imprime un espacio entre las líneas

    print("Hallamos el área del triángulo")
    ba_triangulo = obtener_valor("Ingrese la base del triángulo: ")
    h_triangulo = obtener_valor("Ingrese la altura del triángulo: ")
    area_triangulo = calcular_area_triangulo(ba_triangulo, h_triangulo)
    print("Área del triángulo:", area_triangulo)

main()