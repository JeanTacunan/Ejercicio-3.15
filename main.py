import math


class ConversorAngulos:
    @staticmethod
    def grados_a_radianes(grados: float) -> float:
        return grados * (math.pi / 180)

    @staticmethod
    def radianes_a_grados(radianes: float) -> float:
        return radianes * (180 / math.pi)


def main():
    print("Seleccione el tipo de conversión:")
    print("1. Convertir de grados a radianes")
    print("2. Convertir de radianes a grados")

    opcion = input("Ingrese 1 o 2: ")

    try:
        if opcion == '1':
            grados = float(input("Ingrese el ángulo en grados: "))
            radianes = ConversorAngulos.grados_a_radianes(grados)
            print(f"{grados} grados son {radianes} radianes.")
        elif opcion == '2':
            radianes = float(input("Ingrese el ángulo en radianes: "))
            grados = ConversorAngulos.radianes_a_grados(radianes)
            print(f"{radianes} radianes son {grados} grados.")
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
