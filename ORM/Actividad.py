#import sqlite3

#conn = sqlite3.connect("mi_app.db")
#cursor = conn.cursor()
#cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios ( 
#id INTEGER PRIMARY KEY, 
#nombre TEXT, 
#email TEXT, 
#activo INTEGER ) """) 
#cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana García', 'ana@mail.com', 1)") 
#conn.commit()
# Escribimos el SQL nosotros
#cursor.execute("""
   # SELECT id, nombre, email
    #FROM usuarios
    #WHERE activo = 1
#""")

#rows = cursor.fetchall()

# Convertimos filas a diccionarios a mano
#usuarios = [
 #   {'id': row[0], 'nombre': row[1], 'email': row[2]}
  #  for row in rows
#]

#conn.close()

#from sqlalchemy import Column, Integer, String, Boolean, create_engine
#from sqlalchemy.orm import DeclarativeBase, Session

# 1. Definimos la clase (una sola vez)
#class Base(DeclarativeBase):
 #   pass

#class Usuario(Base):
 #   __tablename__ = "usuarios"

  #  id      = Column(Integer, primary_key=True)
   # nombre  = Column(String)
   # email   = Column(String)
    #activo  = Column(Boolean)

# 2. Consultamos como si fueran objetos Python
#engine = create_engine("sqlite:///mi_app.db")

#with Session(engine) as session:
 #   usuarios = session.query(Usuario) \
  #                    .filter(Usuario.activo == True) \
   #                   .all()

    #for u in usuarios:
     #   print(u.nombre, u.email)  # ← atributos reales, no índices


from sqlalchemy import Column, Integer, String, Boolean, create_engine, or_
from sqlalchemy.orm import DeclarativeBase, Session

# 1. Definimos la clase (una sola vez)
class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "Productos"
    id = Column(Integer, primary_key=True)
    nombre    = Column(String)
    categoria = Column(String)
    stock  = Column(Integer)
    precio = Column(Integer)
    activo=Column(Boolean)

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///mi_app.db")
Base.metadata.create_all(engine)



with Session(engine) as session:
    producto1 = Producto(
        id=1,
        nombre="Teclado mecanico",
        stock=15,
        categoria="Periféricos",
        precio=8500,
        activo=True,
    )

    producto2 = Producto(
        id=2,
        nombre="Mouse inalambrico",
        stock=30,
        categoria="Periféricos",
        precio=4200,
        activo=False,
    )

    producto3 = Producto(
        id=3,
        nombre="Monitor 24 pulgadas",
        stock=8,
        categoria="Pantallas",  
        precio=62000,
        activo=True,
    )

    producto4 = Producto(
        id=4,
        nombre="Auriculares bluetooth",
        precio=12300,
        stock=20,
        categoria="Audio",
        activo=True,
    )

    producto5 = Producto(
        id=5,
        nombre="Webcam Full HD",
        precio=9800,
        stock=12,
        categoria="Periféricos",
        activo=False,
    )

    producto6 = Producto(
        id=6,
        nombre="SSD 1TB",
        precio=18500,
        stock=25,
        categoria="Almacenamiento",
        activo=False,
    )

    producto7 = Producto(
        id=7,
        nombre="RAM 16GB",
        precio=15600,
        stock=18,
        categoria="Componentes",
        activo=True,
    )

    producto8 = Producto(
        id=8,
        nombre="Mousepad XL",
        precio=2100,
        stock=40,
        categoria="Periféricos",
        activo=False,
    )

    
    producto9 = Producto(
        id=9,
        nombre="Hub USB-C",
        precio=5400,
        stock=6,
        categoria="Accesorios",
        activo=False,
    )

    producto10 = Producto(
        id=10,
        nombre="Cable HDMI",
        precio=1800,
        stock=50,
        categoria="Accesorios",
        activo=True,
    )
    producto11 = Producto(
        id=11,
        nombre="Placa de video",
        precio=None,
        stock=50,
        categoria=None,
        activo=True,
    )

    session.add_all([
        producto1,
        producto2,
        producto3,
        producto4,
        producto5,
        producto6,
        producto7,
        producto8,
        producto9,
        producto10,
        producto11,
    ])

    session.commit()

#    with Session(engine) as session:

 #    productos = session.query(Producto) \
  #                     .filter(Producto.precio < 500) \
   #                    .all()

    #print("\nProductos con precio menor a $500:")

    #for producto in productos:
     #   print(
      #      producto.nombre,
       #     "- $", producto.precio,
        #    "- Stock:", producto.stock,
         #   "- Categoría:", producto.categoria,
          #  "- Activo:", producto.activo

        #)

#actividad 3

#productos = session.query(Producto) \
 #                  .filter(Producto.categoria == "Periféricos") \
 #                  .all()

#print("\nProductos de la categoría Periféricos:")

#for producto in productos:
 #   print(
  #      producto.nombre,
   #     "- $", producto.precio
    #)




#actividad 4

    #productos = session.query(Producto) \
     #              .filter(Producto.precio > 10000 ) \
      #             .order_by(Producto.precio.desc()) \
       #            .all()

#print("\nProductos mayores a $10000")

#for producto in productos:
 #   print(
  #      producto.nombre,
   #      "- $", producto.precio,
    #    "- Stock:", producto.stock,
     #  "- Categoría:", producto.categoria,
      #"- Activo:", producto.activo

  #  )
#actividad 5
#productos = session.query(Producto) \
 #                  .filter(Producto.stock <= 12,Producto.activo == True) \
  #                 .all()

#print("\nProductos en stock activos")

#for producto in productos:
 #   print(
  #      producto.nombre,
   #      "- $", producto.precio,
    #    "- Stock:", producto.stock,
     #  "- Categoría:", producto.categoria,
      #"- Activo:", producto.activo

    #)
    #no aparece el producto Hub USB-C ya que el AND es obligatorio
    #que este cumpliendo todas las condiciones puestas, es decir que dicho componente 
    #esta activo pero no cumple con la otra condicion que el stock sea menor o igual a 12

    #actividad 6

   # productos = session.query(Producto) \
    #             .filter(Producto.precio > 5000, Producto.precio < 20000) \
    #               .all()

#print("\nProductos entre $5000 y $20000")

#for producto in productos:
 #   print(
#        producto.nombre,
 #       "- $", producto.precio,
  #      "- Stock:", producto.stock,
   #    "- Categoría:", producto.categoria
    #)

#actividad 7
#producto = session.query(Producto) \
 #                 .order_by(Producto.precio.desc()) \
  #                .first()

#print("\nProducto más caro:")

#print(
 #   producto.nombre,
  #  "- $", producto.precio
#)

#actividad 8
#productos = session.query(Producto) \
        #           .filter(Producto.activo == False) \
          #         .all()

#print("\nProductos en stock activos")

#for producto in productos:
 #   print(
  #      producto.nombre,
   #      "- $", producto.precio,
    #    "- Stock:", producto.stock,
     # "- Activo:", producto.activo

    #)
#actividad final

#producto = session.get(Producto, 9)

#producto.activo = True
#producto.stock = 20

#session.commit()

#print("\nHub USB-C actualizado:")
#print(
 #   producto.nombre,
  #  "- Stock:", producto.stock,
   # "- Activo:", producto.activo
#)

#actividad 9
#productos = session.query(Producto) \
 #                 .filter((Producto.categoria == "Componentes") |
  #                        (Producto.categoria =="Audio")) \
   #               .all()

#print("\nProductos de la categoría Periféricos:")

#for producto in productos:
 #   print(
  #      producto.nombre,
   #     "- $", producto.precio
    #)
#actividad 10
# actividad 10

productos = session.query(Producto) \
                   .filter(Producto.nombre.contains("a")) \
                   .all()

print("\nProductos cuyo nombre contiene la letra 'a':")

for producto in productos:
    print(producto.nombre)

#actividad 11
productos = session.query(Producto) \
                   .filter(Producto.nombre.startswith("m")) \
                   .all()

print("\nProductos cuyo nombre contiene la letra 'm':")

for producto in productos:
    print(producto.nombre)

 #actividad 12
productos = session.query(Producto) \
                   .filter(Producto.categoria == None) \
                   .filter(Producto.precio == None)\
                   .all()

print("\nCategorias nulas:")

for producto in productos:
    print(producto.nombre,
          "-Categoria", producto.categoria,
          "-Precio", producto.precio)
