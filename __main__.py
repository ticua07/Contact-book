#Archivo creado por APC (A Project Creator)
import sqlite3
import os
def add_contact():
    nombre = input("Nombre y apellido> ")
    numero = input("Numero telefonico> ")
    ubicacion = input("Ubicacion> ")
    c.execute(f"""INSERT INTO contacts VALUES ('{nombre}','{numero}','{ubicacion}')""")

def delete_contact():
    nombre = input("Nombre del contacto a borrar> ")
    c.execute(f"""DELETE FROM contacts WHERE nombre = '{nombre}'""")

def search_contact():
    nombre = input("Nombre del contacto a buscar> ")
    for row in c.execute(f"""SELECT * FROM contacts WHERE nombre = '{nombre}'"""):
        print(*row)
def show_all():
    for row in c.execute(f'SELECT * FROM contacts'):
        print(*row, sep="|")
        print("-----------------")
conn = sqlite3.connect('contacts.db') # crea la conexion a 'contacts.db'
c = conn.cursor() # crea el cursor
try:
    c.execute("""CREATE TABLE contacts (nombre text, telefono text, Ubicacion text)""")
except sqlite3.OperationalError:
    pass

print("""
1. Añadir contacto
2. Borrar contacto
3. Buscar contacto por su nombre y apellido
4. Mostrar todos los contactos
5. Salir
""")
ans = int(input("Que desea hacer> "))

if ans == 1: # añadir contacto
    add_contact()
elif ans == 2: # borrar contacto
    delete_contact()
elif ans == 3: # Buscar contacto
    search_contact()
elif ans == 4: # Mostrar todos los contactos
    show_all()
elif ans == 5: # Salir
    conn.commit()
    conn.close()
    exit()


conn.commit() # guarda los cambios
conn.close() # cierra 'contacts.db'