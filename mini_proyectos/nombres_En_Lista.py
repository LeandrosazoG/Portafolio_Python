

list_name=[]



while True:
    print(      "Menu "
      "\n1 enter  name : "
      "\n2 Delete name : "
      "\n3 exit : ")


    option =  int(input("choose your option : "))



    if option == 1:
        n=int(input("How many names are you going to enter : ? "))
        for i in range(n):
            name= input(f"enter your name # {i+1}")
            list_name.append(name)
            print(list_name )

    elif option == 2:
        n=int(input("How many names will you eliminate? : "))
        for i in range(n):
            name_to_delete = input("enter the name to delete  :")
            found = False
            for existing in list_name:
                if existing.lower()== name_to_delete.lower():
                    list_name.remove(existing)
                    print(list_name)
                    found = True
                    break
            if not found:
                  print(f"❌ Name '{name_to_delete}' not found in the list.")
        print("Current list:", list_name)


    elif option == 3:
        print("Exiting program. Goodbye!")
        break


    


#####found te permite mostrar un mensaje de error personalizado si no se encontró nada
