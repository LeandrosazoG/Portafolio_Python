import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from conexion import *
from clientes import *



class FormularioUsuarios:
    global Base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxNombre 
    textBoxNombre = None

    global textBoxApellido
    textBoxApellido = None

    global textBoxEdad 
    textBoxEdad = None

    global textBoxSexo
    textBoxSexo = None
    
    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None


def Formulario():
    global textBoxId
    global textBoxNombre
    global textBoxApellido
    global textBoxEdad
    global textBoxSexo
    global combo
    global base
    global groupBox
    global tree


    try:
        base = Tk()
        base.geometry("1450x300")
        base.title("CRUD python + SQLite")


        groupBox =LabelFrame(base, text="Datos del Usuario",padx=5, pady=5)
        groupBox.grid(row=0,column=0, padx=10,pady=10)

        LabelId=Label(groupBox, text="Id:",width=13,font=("Arial", 12)).grid(row=0,column=0,)
        textBoxId=Entry(groupBox)
        textBoxId.grid(row=0,column=1)

        LabelNombres=Label(groupBox, text="Nombres:",width=13,font=("Arial", 12)).grid(row=1,column=0,)
        textBoxNombre=Entry(groupBox)
        textBoxNombre.grid(row=1,column=1)

        LabelApellidos=Label(groupBox, text="Apellidos:",width=13,font=("Arial", 12)).grid(row=2,column=0,)
        textBoxApellido=Entry(groupBox)
        textBoxApellido.grid(row=2,column=1)



        LabelEdad=Label(groupBox, text="Edad:",width=13,font=("Arial", 12)).grid(row=3,column=0,)
        textBoxEdad=Entry(groupBox)
        textBoxEdad.grid(row=3,column=1)
        

        
        LabelSexo=Label(groupBox, text="sexo:",width=13,font=("Arial", 12)).grid(row=4,column=0,)
        seleccionSexo = tk.StringVar()

        
        combo = ttk.Combobox(groupBox,values = ["Masculino", "Femenino"], textvariable=seleccionSexo)
        combo.grid(row=4,column=1)
        seleccionSexo.set("masculino")


        Button(groupBox, text="Guardar",width=10,command=guardarRegistro).grid(row=5,column=0)
        Button(groupBox, text="Modificar",width=10,command=ModificarRegistro).grid(row=5,column=1)
        Button(groupBox, text="Eliminar",width=10,command=EleminarUsuario).grid(row=5,column=2)


        groupBox =LabelFrame(base, text="Lista de Usuarios",padx=5, pady=5)
        groupBox.grid(row=0,column=1,padx=5,pady=5)


        tree = ttk.Treeview(groupBox,columns=("id","nombre","apellido","edad","sexo"),show="headings", height=5,)
        tree.column('#1', anchor=CENTER)
        tree.heading('#1',text='Id')
        tree.column('#2', anchor=CENTER)
        tree.heading('#2',text='Nombres')
        tree.column('#3', anchor=CENTER)
        tree.heading('#3',text='Apellidos')
        tree.column('#4', anchor=CENTER)
        tree.heading('#4',text='Sexo')
        tree.column('#5', anchor=CENTER)
        tree.heading('#5',text='Edad')


        vsb = Scrollbar(groupBox, orient="vertical",command=tree.yview) ##  Scrollbar para el Treeview

        tree.configure(yscrollcommand=vsb.set)

        tree.pack(side=LEFT,fill=BOTH,expand=TRUE)
        vsb.pack(side=RIGHT,fill=Y)

        ##aqui llenamos la tabla  desde la base de datos 


        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)

        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)



        base.mainloop()
    except ValueError as error :
        print("Error al crear la interfaz:", error)

def guardarRegistro():
    global textBoxNombre
    global textBoxApellido
    global textBoxEdad
    global combo
    global groupBox

    try:
        if (textBoxNombre is None or textBoxApellido is None 
            or textBoxEdad is None or combo is None):
            print("Los widgets no están inicializados correctamente")
            return
        
        nombre = textBoxNombre.get()
        apellido = textBoxApellido.get()
        sexo = combo.get()
        edad = textBoxEdad.get()

        CClientes.ingresarUsuario(nombre, apellido, sexo, edad)
        messagebox.showinfo("Éxito", "Usuario guardado correctamente")

        actualizarTreeview()

        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)  
        textBoxEdad.delete(0, END)

    except ValueError as error:
        print(f"Error al consultar los clientes: {error}")
        return None
       


def actualizarTreeview():

    global tree

    try:
        tree.delete(*tree.get_children())

        datos = CClientes.mostrarClientes()


        
        for row in CClientes.mostrarClientes():
         tree.insert("","end",values=row)

    except ValueError as error:
        print(f"Error al consultar los clientes: {error}")
        return None
       

def seleccionarRegistro(evento):
    try:
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            value = tree.item(itemSeleccionado)['values']

            textBoxId.delete(0, END)
            textBoxId.insert(0, value[0])

            textBoxNombre.delete(0, END)
            textBoxNombre.insert(0, value[1])

            textBoxApellido.delete(0, END)
            textBoxApellido.insert(0, value[2])

             
            textBoxEdad.delete(0, END)
            textBoxEdad.insert(0, value[3])

            combo.set(value[4])

    except ValueError as error:
        print(f"Error al consultar los clientes: {error}")
        return None     
    



def ModificarRegistro():
    global textBoxId
    global textBoxNombre
    global textBoxApellido
    global textBoxEdad
    global combo
    global groupBox

    try:
        if ( textBoxId is NONE or textBoxNombre is None or textBoxApellido is None 
            or textBoxEdad is None or combo is None):
            print("Los widgets no están inicializados correctamente")
            return
        idUsuario = textBoxId.get()
        nombre = textBoxNombre.get()
        apellido = textBoxApellido.get()
        sexo = combo.get()
        edad = textBoxEdad.get()

        CClientes.ModificarUsuario(idUsuario,nombre, apellido, sexo, edad)
        messagebox.showinfo("Éxito", "Usuario modificado correctamente")

        actualizarTreeview()

        textBoxId.delete(0, END)
        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)  
        textBoxEdad.delete(0, END)
        combo.set("masculino")

    except ValueError as error:
        print(f"Error al consultar los clientes: {error}")
        return None
       



def EleminarUsuario():
    
    global textBoxId
    global textBoxNombre
    global textBoxApellido
    global textBoxEdad
    global combo
    global groupBox

    try:
        if ( textBoxId is None):
            print("Los widgets no están inicializados correctamente")
            return
        
        idUsuario = textBoxId.get()
        

        CClientes.EliminarUsuario(idUsuario,)
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente")

        actualizarTreeview()

        textBoxId.delete(0, END)
        textBoxNombre.delete(0, END)
        textBoxApellido.delete(0, END)  
        textBoxEdad.delete(0, END)
        combo.set("masculino")

    except ValueError as error:
        print(f"Error al consultar los clientes: {error}")
        return None

    



Formulario()







