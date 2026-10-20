from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Categoria(Base):
    __tablename__ = "categorias"


    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"


    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    tela = Column(String, nullable=False)
    precio_base = Column(Float, nullable=False)
    activo = Column(Boolean, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))


    categoria = relationship("Categoria", back_populates="productos")
    variantes = relationship("Variante", back_populates="producto")


class Variante(Base):
    __tablename__ = "variantes"


    id = Column(Integer, primary_key=True)
    sku = Column(String, nullable=False)
    talle = Column(String, nullable=False)
    color = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"))


    producto = relationship("Producto", back_populates="variantes")
    detalles = relationship("DetallePedido", back_populates="variante")


class Cliente(Base):
    __tablename__ = "clientes"


    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)


    pedidos = relationship("Pedido", back_populates="cliente")


class Pedido(Base):
    __tablename__ = "pedidos"


    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    estado = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))


    cliente = relationship("Cliente", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido")


class DetallePedido(Base):
    __tablename__ = "detalle_pedido"


    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    variante_id = Column(Integer, ForeignKey("variantes.id"))


    pedido = relationship("Pedido", back_populates="detalles")
    variante = relationship("Variante", back_populates="detalles")


engine = create_engine("sqlite:///uniformes.db",
                       echo=True)


Base.metadata.create_all(engine)