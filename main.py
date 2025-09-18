

def addmultiplenumbers(lista_de_num):
    return sum(lista_de_num)

def multiplymultiplenumbers(lista_de_num):
    resultado = 1
    for num in lista_de_num:
        resultado *= num
    return resultado

def isiteven(num):
    if isinstance(num, int):  
        return num % 2 == 0
    return False
    

def isitaninteger(valor):
    return isinstance(valor, int)

def main():
    print("Hello learners!")
    numeros = [1,2,3,4]
    print("suma:", addmultiplenumbers(numeros))
    print("multiplicacion:", multiplymultiplenumbers(numeros))
    print(isiteven(4))
    print(isiteven(5))
    print(isitaninteger(3))
if __name__=="__main__":
  main()