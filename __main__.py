import sqlite3
import os

def add_contact():
    clear = os.system("cls") if os.name == "nt" else os.system("clear")
    nombre = input("Nombre> ")
    telefono = input("Telefono> ")
    ubicacion = input("Ubicacion> ")
    c.execute(f"INSERT INTO contacts VALUES (Null,'{nombre}','{telefono}','{ubicacion}')")

def delete_contact():
    clear = os.system("cls") if os.name == "nt" else os.system("clear")
    nombre = input("Buscar por nombre> ")
    for i in c.execute(f"SELECT * FROM contacts WHERE nombre = '{nombre}'"):
        print(type(i))
        print(*i, sep=" | ")
        print("Quieres eliminar ese contacto?")
        ans = input("(s/n)> ")
        if ans == "s":
            c.execute(f"DELETE FROM contacts WHERE id = '{i[0]}'")
        elif ans == "n":
            exit()
        else:
            print('"' + ans + '"', "no es una respuesta")
            exit()
    
def search_contact():
    clear = os.system("cls") if os.name == "nt" else os.system("clear")
    nombre = input("Nombre> ")
    data = []
    for i in c.execute(f"SELECT nombre, telefono, ubicacion, id FROM contacts WHERE nombre = '{nombre}'"):
        if i == i[3]:
            break
        else:
            data.append(i)
    print(*data, sep=" | ")

def show_all_contacts():
    clear = os.system("cls") if os.name == "nt" else os.system("clear")
    for i in c.execute("SELECT * FROM contacts"):
        print(*i, sep=" | ")
        print("----------------------------------------------------------")


conn = sqlite3.connect("Contacts.db")
c = conn.cursor()
try:
    c.execute("CREATE TABLE contacts (id integer PRIMARY KEY, nombre text, telefono text, ubicacion text)")
except Exception as ex:
    pass

print("1. Añadir contacto")
print("2. Borrar contacto")
print("3. Buscar contacto")
print("4. Mostrar todos los contactos")
print("5. Salir")
ans = int(input("> "))
if ans == 1:
    add_contact()
elif ans == 2:
    delete_contact()
elif ans == 3:
    search_contact()
elif ans == 4:
    show_all_contacts()
elif ans == 5:
    print("Saliendo")
    exit()
else:
    print(ans, "no es una respuesta correcta!")

conn.commit()
conn.close()
