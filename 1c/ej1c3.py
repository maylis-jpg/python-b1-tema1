"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7

"""


def find_max(lst):
    # Write here your code

    result = []

    if len(lst) == 1:
        return lst[0]
    if lst[0] < find_max(lst[1:]):
        result = find_max(lst[1:])
    else:
        result = lst[0]
    
    return result


    pass

numbers_list = [1, 5, 2, 7, 3]
print(find_max(numbers_list))
