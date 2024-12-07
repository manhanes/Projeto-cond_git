# Solicitar os valores e a operação matemática
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação matemática (+, -, *, /): ")

# Realizar o cálculo com base na operação informada
if operacao == "+":
    resultado = valor1 + valor2
elif operacao == "-":
    resultado = valor1 - valor2
elif operacao == "*":
    resultado = valor1 * valor2
elif operacao == "/":
    # Verificar se o divisor é diferente de zero
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."

# Exibir o resultado
print("O resultado é:", resultado)
