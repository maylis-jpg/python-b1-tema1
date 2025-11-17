'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

'''

def count_vowels(text_chain:str):
    # Write here your code

    count = 0
    
    for letra in text_chain:
        if letra in 'aeiouAEIOU':
            count += 1
    
    return count

    pass

print(count_vowels("Hello world, this is an example."))
