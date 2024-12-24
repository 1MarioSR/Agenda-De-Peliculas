from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    sql = """
    CREATE TABLE peliculas(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50),
        duracion VARCHAR(10),
        genero VARCHAR(50)
    )"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se Creo La Tabla En La Base De Datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La Tabla Ya Esta Creada"
        messagebox.showwarning(titulo, mensaje)
        

def borrar_tabla():
   conexion = ConexionDB()

   sql = "DROP TABLE peliculas"
   try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "La Tabla De La Base De Datos Se Borro Con Éxito"
        messagebox.showwarning(titulo, mensaje)
   except:  
        titulo = "Borrar Registro"
        mensaje = "No Hay Tabla Para Borrar"
        messagebox.showerror(titulo, mensaje)
        
class Pelicula:
    def __init__(self, nombre, duracion, genero):
      self.id = None
      self.nombre = nombre
      self.duracion = duracion
      self.genero = genero

    def __str__(self):
        return f"pelicula[{self.nombre},{self.duracion},{self.genero}]"

def guardar(pelicula):
    conexion = ConexionDB()
        
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES("{pelicula.nombre}", "{pelicula.duracion}", "{pelicula.genero}")"""
    
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except: 
        titulo = "Conexion Al Registro"
        mensaje = "La Tabla Peliculas No Esta Creada En La Base De Datos"
        messagebox.showerror(titulo, mensaje)
        
def listar():
    conexion = ConexionDB()

    lista_peliculas = []
    sql = "SELECT * FROM peliculas"

    try: 
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion Al Registro"
        mensaje = "Crea La Tabla En La Base De Datos"
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas


def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
   
    sql = f"""UPDATE peliculas SET nombre = "{pelicula.nombre}", duracion = "{pelicula.duracion}", genero = "{pelicula.genero}" WHERE id = {id_pelicula}"""

    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = "Edición De Datos"
        mensaje = "No Se Ha Podido Editar Este Registro"
        messagebox.showerror(titulo, mensaje)
        
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f"DELETE  FROM peliculas WHERE id = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar Datos"
        mensaje = "No Se Pudo Eliminar El Registro"
        messagebox.showerror(titulo, mensaje)