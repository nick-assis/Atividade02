def calculadora(num1, num2, opcao):
    if(opcao == 1):
     return num1 + num2
    elif(opcao == 2):
     return num1 - num2
    elif(opcao == 3):
     return num1 * num2
    elif (opcao == 4):
     return num1 / num2
    else:
      return  0

result = calculadora(23, 4, 3)
print(result)

