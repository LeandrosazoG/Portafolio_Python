
###### anagaramas ver una funcion con dos variables que te digan si son una anagrama

def is_anagram(palabra1,palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

  


print(is_anagram("amor","roma"))
