import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS 
    ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
      NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
      PRECIO INTEGER NOT NULL,
      SECCION VARCHAR(20) NOT NULL)
    ''')

productos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria"),
    ("Pelota", 25, "Deportes")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



miConexion.commit()
miConexion.close()