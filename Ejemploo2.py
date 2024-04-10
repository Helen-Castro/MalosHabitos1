"Castro Arteaga Helen-Rojas Ortiz Franklin"
def calcular_producto_suma(a, b, c):
    return a * b + c


def principal():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))
    z = int(input("Ingrese el valor de z: "))

    resultado = calcular_producto_suma(x, y, z)
    print("El resultado es:", resultado)


if __name__ == "__main__":
    principal()