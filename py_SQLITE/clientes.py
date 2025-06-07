from conexion import *

class CClientes:
    def mostrarClientes():
        try:
            cone = Cconexion.ConexionBaseDeDatos()
            consulta= cone.cursor()
            consulta.execute("SELECT * FROM USUARIOS;")
            miResultado = consulta.fetchall()
            cone.close()
            return miResultado
        except sqlite3.Error as error: 
            print(f"Error al consultar los clientes:{error}")
            return None


    def ingresarUsuario(nombres,apellidos,sexo,edad): 

        try:
            cone = Cconexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql = "INSERT INTO usuarios values (null,?,?,?,?)"

            valores = (nombres,apellidos,sexo,edad)
            consulta.execute(sql, valores)
            cone.commit()
            print(consulta.rowcount, "Usuario ingresado correctamente")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al consultar los clientes:{error}")
            return None
        
    def ModificarUsuario(idUsuario,nombres,apellidos,sexo,edad): 

        try:
            cone = Cconexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql = "UPDATE usuarios SET nombres= ?, apellidos=?, sexo=?, edad=? WHERE id=?"

            valores = (nombres,apellidos,sexo,edad, idUsuario)
            consulta.execute(sql, valores)
            cone.commit()
            print(consulta.rowcount, "Registro modificado correctamente")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al actualizar :{error}")
            return None
        

    def EliminarUsuario(idUsuario): 

        try:
            cone = Cconexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql = "DELETE FROM usuarios WHERE id=?"
            valores = (idUsuario,)
            consulta.execute(sql, valores)
            cone.commit()
            print(consulta.rowcount, "Registro eliminado correctamente")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al actualizar :{error}")
            return None