"""
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30
"""

def sum_odd_numbers(list_numbers):
    # Validación list_numebers, si no numerico o menor cero = ValueError('mensage')

    for i in list_numbers:
        if not isinstance(i, int):
            raise ValueError('Introduir valor numérico')
        if i < 0:
            raise ValueError('Introduir valor numérico mayor o igual a cero')
    
    # Devolver la suma de los números impares encontrados en la lista

    result = 0

    for i in list_numbers:
        if i % 2 != 0:
            result += i
    
    return result 
    pass

# print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
