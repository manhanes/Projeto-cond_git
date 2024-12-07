string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repetir a string com espaços entre elas
resultado = (string + " ") * numero

# Remover o espaço extra ao final
resultado = resultado.strip()

print(resultado)
