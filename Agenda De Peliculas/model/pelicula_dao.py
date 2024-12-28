from .conexion_db import ConexionDB
from tkinter import messagebox
import csv
from tkinter import filedialog

#En Esta Parte Del Codigo Se Crean Los Querys Para La Base De Datos Y Se Crean Las Bases De Datos
def crear_tabla():
    conexion = ConexionDB()
    
    sql = """
    CREATE TABLE IF NOT EXISTS peliculas(
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
    sql_check_table = "SELECT name FROM sqlite_master WHERE type='table' AND name='peliculas';"
    sql = " SELECT * FROM peliculas"

    try: 
        conexion.cursor.execute(sql_check_table)
        table_exists = conexion.cursor.fetchone()
        
        if table_exists:
            conexion.cursor.execute(sql)
            lista_peliculas = conexion.cursor.fetchall()
        else:
            titulo = "Conexion Al Registro"
            mensaje = "La Tabla Peliculas No Esta Creada En La Base De Datos"
        
        conexion.cerrar()
    except Exception as e:
        titulo = "Conexion Al Registro"
        mensaje = "La Tabla Peliculas No Esta Creada En La Base De Datos"
        messagebox.showerror(titulo, mensaje)
        
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
        
def listar_registro():
    conexion = ConexionDB()
    sql = "SELECT * FROM peliculas"
    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()
        conexion.cerrar()

        if registros:
            mensaje = "\n".join([f"ID: {row[0]}, Título: {row[1]}, Duración: {row[2]} min, Género: {row[3]}" for row in registros])
        else:
            mensaje = "No hay registros en la tabla."

        messagebox.showinfo("Lista de Películas", mensaje)

    except Exception as e:
        messagebox.showerror("Error al listar", f"No se pudieron obtener los datos: {e}")

def exportar_registro():
    conexion = ConexionDB()
    sql = "SELECT * FROM peliculas"

    try:
        conexion.cursor.execute(sql)
        registros = conexion.cursor.fetchall()

        if not registros:
            messagebox.showinfo("Exportar Registros", "No hay registros en la tabla.")
            return

        
        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if archivo:
            with open(archivo, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "Duracion", "Genero"])  
                writer.writerows(registros)  

            messagebox.showinfo("Exportar Registros", "Registros exportados exitosamente.")
        
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror("Error al exportar", f"No se pudieron exportar los datos: {e}")
        
        
        
def peliculas_por_genero():
    conexion = ConexionDB()
    try:
        sql = "SELECT genero, COUNT(*) FROM peliculas GROUP BY genero"
        conexion.cursor.execute(sql)
        resultados = conexion.cursor.fetchall()
        conexion.cerrar()

        if resultados:
            mensaje = "\n".join([f"{genero}: {conteo} películas" for genero, conteo in resultados])
            messagebox.showinfo("Estadísticas por Género", mensaje)
        else:
            messagebox.showinfo("Sin Datos", "No hay películas registradas para generar estadísticas.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron generar las estadísticas: {e}")


def duracion_promedio():
    conexion = ConexionDB()
    try:
        sql = "SELECT AVG(duracion) FROM peliculas"
        conexion.cursor.execute(sql)
        promedio = conexion.cursor.fetchone()[0]
        conexion.cerrar()

        if promedio:
            messagebox.showinfo("Duración Promedio", f"La duración promedio de las películas es de {round(promedio, 2)} minutos.")
        else:
            messagebox.showinfo("Sin Datos", "No hay películas registradas para calcular la duración promedio.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo calcular la duración promedio: {e}")


def total_peliculas():
    conexion = ConexionDB()
    try:
        sql = "SELECT COUNT(*) FROM peliculas"
        conexion.cursor.execute(sql)
        total = conexion.cursor.fetchone()[0]
        conexion.cerrar()

        messagebox.showinfo("Total de Películas", f"Total de películas registradas: {total}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo calcular el total de películas: {e}")

        
        

def manual():
    mensaje = """Este es un programa de gestión de películas. Puede agregar, editar, eliminar y listar películas. También puede exportar los registros a un archivo CSV y ver estadísticas sobre las películas registradas.
            Manual de Uso de la Agenda de Películas**
        1. Agregar Película: Ingrese el título, género y año y presione 'Guardar'.
        2. Buscar Película: Use el cuadro de búsqueda para encontrar una película por título.
        3. Editar Película: Seleccione una película y haga clic en 'Editar'.
        4. Eliminar Película: Seleccione una película y presione 'Eliminar'."""
    titulo = "Manual de Usuario"
    messagebox.showinfo(titulo, mensaje)



def contacto():
    mensaje = "Desarrollado Por: Mario Suero\nCorreo: mario.suerodejesus@gmail.com"
    titulo = "Contacto"
    messagebox.showinfo(titulo, mensaje)