import sqlite3
import os

class Cconexion:
    @staticmethod
    def ConexionBaseDeDatos():
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))  # Carpeta donde está conexion.py
            ruta_db = os.path.join(base_dir, "DBusuarios.db")      # Archivo de la base dentro de esa carpeta

            conexion = sqlite3.connect(ruta_db)
            print("Conexión exitosa a la base de datos.")
            return conexion
        except sqlite3.error as error:
            print("Error al conectar a la base de datos:", error)
            return None
        
Cconexion.ConexionBaseDeDatos()


