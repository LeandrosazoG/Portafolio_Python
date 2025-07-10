
# palabra = input("ingresa una palabra")

# rev=palabra[::-1]

# print(f"la palabra al reves es: {rev}")




# ### con funcion 

def reverse(text):
    text_len = len(text)
    reversed_text =" "
    for index in range(0, text_len):
        reversed_text += text[text_len - index -1]
    return reversed_text

print(reverse("hola mundo"))