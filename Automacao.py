#menu1

print("Bebidas: ")
print("1 - Coca 1 litro R$ 8.00")
print("2 - Fanta lata R$ 5.00")
print("3 - Sem bebida R$ 0.00")
bebida = int(input("Escolha uma bebida: "))
if bebida == 1:
    resultb = 8
elif bebida == 2:
    resultb = 5
elif bebida == 3:
    resultb == 0
else:
    print("Escolha uma das opções")

#menu2

print(" ")
print("Pizza: ")
print("1 - Pizza de calabresa R$ 30.00")
print("2 - Pizza de queijo e presunto R$ 25.00")
print("3 - Sem pizza R$ 0.00")
pizza = int(input("Escolha uma pizza: "))
if pizza == 1:
    resultp = 30
elif pizza == 2:
    resultp = 25
elif pizza == 3:
    resultp = 0
else:
    print("Escolha uma das opções")

#Dados do cliente
print(" ")
print("Finalize seu pedido: ")
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")

#Calculo do total
total = resultb + resultp 

#CheckOut

print(" ")
print(" * * * * Nota Fiscal * * * * ")
print(" ")
print(" * * * * Dados do Cliente * * * * ")
print("Nome do cliente: " + nome)
print("Endereço: "+ endereco)
print(" ")
print(" * * * * Pedido * * * *")
print("Bebida: " + "R$: " + str(resultb))
print("Pizza: " + "R$: " + str(resultp))
print("Subtotal: "+ "R$: " + str(total))
print(" ")
print(" * * * * Fim do Pedido * * * * ")