'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

'''

def invert_text(text_chain:str):
    # Write here your code

    inv_text = ''
    
    for letra in text_chain[::-1]:
        inv_text += letra
    
    return inv_text
    pass

print(invert_text("Hello world!"))
