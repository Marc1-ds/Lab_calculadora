def sumar(lista):
    return sum(lista)

def multiplicar(lista):
    """Recibe una lista de números y devuelve el producto total."""
    resultado = 1
    for numero in lista:
        resultado *= numero
    return 