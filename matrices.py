class Matriz:
    def __init__(self):
        self.matriz = []
        self.filas = 0
        self.columnas = 0

    def solicitar_dimension(self):
        # Método para solicitar las dimensiones de la matriz al usuario
        self.filas = int(input("Ingrese el número de filas: "))
        self.columnas = int(input("Ingrese el número de columnas: "))
        # Inicializamos la matriz con ceros
        self.matriz = [[0 for j in range(self.columnas)] for i in range(self.filas)]

    def llenar_matriz(self):
        # Método para llenar la matriz con valores ingresados por el usuario
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

    def mostrar_matriz(self):
        # Método para mostrar la matriz
        print("\nLa matriz es:")
        for fila in self.matriz:
            for elemento in fila:
                print(f"{elemento:4}", end=" ")
            print()  # Salto de línea al final de cada fila

    def mostrar_pares(self):
        # Método para mostrar los números pares de la matriz
        print("\nNúmeros pares en la matriz:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] % 2 == 0:
                    print(f"Posición [{i}][{j}]: {self.matriz[i][j]}")

    def mostrar_impares(self):
        # Método para mostrar los números impares de la matriz
        print("\nNúmeros impares en la matriz:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] % 2 != 0:
                    print(f"Posición [{i}][{j}]: {self.matriz[i][j]}")

# Código para ejecutar el programa
if __name__ == "__main__":
    # Crear una instancia de la clase Matriz
    mi_matriz = Matriz()
    
    # Solicitar dimensiones y llenar la matriz
    mi_matriz.solicitar_dimension()
    mi_matriz.llenar_matriz()
    
    # Mostrar la matriz y sus números pares e impares
    mi_matriz.mostrar_matriz()
    mi_matriz.mostrar_pares()
    mi_matriz.mostrar_impares()
