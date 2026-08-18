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
    stock  = Column(String)
    precio = Column(Boolean)

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///mi_app.db")

with Session(engine) as session:
    

    producto1 = Producto(
        nombre="Teclado",
        precio=450,
        stock=10,
        categoria="Periféricos"
    )

    producto2 = Producto(
        nombre="Mouse",
        precio=300,
        stock=15,
        categoria="Periféricos"
    )

    producto3 = Producto(
        nombre="Monitor",
        precio=1200,
        stock=5,
        categoria="Pantallas"
    )

    producto4 = Producto(
        nombre="Auriculares",
        precio=400,
        stock=8,
        categoria="Audio"
    )

    producto5 = Producto(
        nombre="Webcam",
        precio=600,
        stock=6,
        categoria="Cámaras"
    )

    session.add_all([
        producto1,
        producto2,
        producto3,
        producto4,
        producto5
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
            "- Categoría:", producto.categoria
        )