import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_cfe9ac8ca4964dfc84d6663e11372d6f@localhost:57852")  # Substitua pelo URI do servidor correto
    resultado_somar = calculadora.somar(85, 3)
    resultado_subtrair = calculadora.subtrair(10, 10)
    resultado_multiplicar = calculadora.multiplicar(10, 5)

    print("A soma é:", resultado_somar)
    print("A subtração é:", resultado_subtrair)
    print("A multiplicação é:", resultado_multiplicar)

if __name__ == "__main__":
    main()
