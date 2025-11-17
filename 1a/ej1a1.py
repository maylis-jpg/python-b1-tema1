'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

'''

def fibonacci(fibonacci_number):
    # Validación fibonacci_number, si no numerico o menor cero = ValueError('mensage')

    if not isinstance(fibonacci_number, int):
        raise ValueError('Introduir valor numérico')
    
    if fibonacci_number < 0:
        raise ValueError('Introduir valor numérico mayor a cero')
    
    # Calcular serie fibonacci

    result = 0
    a = 0
    b = 1

    if fibonacci_number == 0:
        result = a
    if fibonacci_number == 1:
        result = b

    for i in range(2, fibonacci_number + 1):
        result = a + b
        a = b
        b = result
                
    return result            
    pass

# print(fibonacci(4))
