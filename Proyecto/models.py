from sqlalchemy import Column, Integer, String, Boolean, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, engine


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(255), nullable=True)
    tela = Column(String(100), nullable=False)
    precio_base = Column(Float, nullable=False)
    activo = Column(Boolean, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="productos")
    variantes = relationship("Variante", back_populates="producto")


class Variante(Base):
    __tablename__ = "variantes"

    id = Column(Integer, primary_key=True)
    sku = Column(String(50), nullable=False)
    talle = Column(String(20), nullable=False)
    color = Column(String(50), nullable=False)
    stock = Column(Integer, nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"))

    producto = relationship("Producto", back_populates="variantes")
    detalles = relationship("DetallePedido", back_populates="variante")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    tipo = Column(String(20), nullable=False)
    email = Column(String(150), nullable=False)
    telefono = Column(String(30), nullable=True)
    direccion = Column(String(255), nullable=True)

    pedidos = relationship("Pedido", back_populates="cliente")


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    estado = Column(String(20), nullable=False)
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


Base.metadata.create_all(engine)