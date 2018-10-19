def hello_world():
    return 'Hello World'

def cria_lista(tam):
    lista = []
    for i in range(tam):
        lista.append(i)

    return lista

def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
        
    a, b = 0, 1
    list_fib = []
    while a <= n:
        list_fib.append(a)
        print(a, end=' ')
        a, b = b, a+b
    print()

    return list_fib