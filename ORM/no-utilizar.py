from sqlalchemy import Column, Integer, String, Boolean, create_engine
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
    activo= Column(Boolean)

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///mi_app.db")

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
    ])


    with Session(engine) as session:

     productos = session.query(Producto) \
                       .filter(Producto.precio < 500) \
                       .all()

    print("\nProductos con precio menor a $500:")

    for producto in productos:
        print(
            producto.nombre,
            "- $", producto.precio,
            "- Stock:", producto.stock,
            "- Categoría:", producto.categoria,
            "- Activo:", producto.activo

        )

#actividad 3
productos = session.query(Producto) \
                   .filter(Producto.categoria == "Periféricos") \
                   .all()

print("\nProductos de la categoría Periféricos:")

for producto in productos:
    print(
        producto.nombre,
        "- $", producto.precio
    )

