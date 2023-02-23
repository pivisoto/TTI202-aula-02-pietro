a = int (input("escolha o metodo desejado 1 - adição , 2 - subtração , 3 - multiplicação , 4 - divisão = "))
b , c = input("digite os valores desejados = ").split(" ")
if (a == 1): 
    print (float(b) + float(c))
elif (a == 2):
    print (float(b) - float(c))
elif (a == 3):
    print (float(b) * float(c))
else:
    print (float(b) / float(c))
