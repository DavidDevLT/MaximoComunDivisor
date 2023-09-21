class NumeroNegativoException(Exception):

    pass
class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self.numeroNatural1 = int(input("Ingrese primer número natural: "))
                if self.numeroNatural1 < 0:
                    raise NumeroNegativoException
                break
            except ValueError as err:
                print("Oops! Ingrese un número entero. Intente otra vez...")
            except NumeroNegativoException as err:
                print("Oops! Ingrese un número entero y positivo. Intente otra vez...")

        while True:
            try:
                self.numeroNatural2 = int(input("Ingrese segundo número natural: "))
                if self.numeroNatural2 < 0:
                    raise NumeroNegativoException
                break
            except ValueError as err:
                print("Oops! Ingrese un número entero. Intente otra vez...")
            except NumeroNegativoException as err:
                print("Oops! Ingrese un número entero y positivo. Intente otra vez...")

        return self.numeroNatural1, self.numeroNatural2

    def maximocomundivisor(self, productodivisores1, productodivisores2):
        numero1 = self.numeroNatural1
        numero2 = self.numeroNatural2
        for divisor in range(1, numero1 + 1):
            if (numero1 % divisor) == 0:
                print("Divisores primer número:")
                print(divisor, "es divisor")
                productodivisores1 *= divisor
                print()
        for divisor in range(1, numero2 + 1):
            if (numero2 % divisor) == 0:
                print("Sivisores segundo número")
                print(divisor, "es divisor")
                print()
                productodivisores2 *= divisor
        mxc = productodivisores1 * productodivisores2
        print(f"El máximo común divisor de ({numero1},{numero2}) es: {mxc}")

