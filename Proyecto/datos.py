from datetime import date
from sqlalchemy.orm import sessionmaker
from schema import engine, Categoria, Producto, Variante, Cliente, Pedido, DetallePedido


Session = sessionmaker(bind=engine)
session = Session()


# 1. Categorías (10)
categorias = [
    Categoria(nombre="Ambos"),
    Categoria(nombre="Chaquetas"),
    Categoria(nombre="Pantalones"),
    Categoria(nombre="Guardapolvos"),
    Categoria(nombre="Gorros"),
    Categoria(nombre="Calzado"),
    Categoria(nombre="Casacas"),
    Categoria(nombre="Barbijos"),
    Categoria(nombre="Medias de compresión"),
    Categoria(nombre="Accesorios")
]
session.add_all(categorias)
session.commit()


# 2. Productos (10)
productos = [
    Producto(nombre="Ambo Classic", descripcion="Ambo de corte clásico, unisex", tela="Spandex antifluido", precio_base=35000, activo=True, categoria_id=1),
    Producto(nombre="Ambo Jogger", descripcion="Pantalón jogger con puño elastizado", tela="Microfibra elastizada", precio_base=42000, activo=True, categoria_id=1),
    Producto(nombre="Chaqueta Térmica", descripcion="Chaqueta con interior polar", tela="Polar", precio_base=28000, activo=True, categoria_id=2),
    Producto(nombre="Pantalón Cargo", descripcion="Pantalón con bolsillos laterales", tela="Gabardina", precio_base=18000, activo=True, categoria_id=3),
    Producto(nombre="Guardapolvo Clásico", descripcion="Guardapolvo manga larga con botones", tela="Gabardina", precio_base=25000, activo=True, categoria_id=4),
    Producto(nombre="Gorro Quirúrgico", descripcion="Gorro de algodón con estampado", tela="Algodón", precio_base=4500, activo=True, categoria_id=5),
    Producto(nombre="Zueco Antideslizante", descripcion="Calzado hospitalario lavable", tela="EVA", precio_base=32000, activo=True, categoria_id=6),
    Producto(nombre="Casaca Cuello V", descripcion="Casaca con tres bolsillos", tela="Spandex antifluido", precio_base=20000, activo=True, categoria_id=7),
    Producto(nombre="Barbijo Tricapa x50", descripcion="Caja de 50 barbijos descartables", tela="TNT", precio_base=6000, activo=True, categoria_id=8),
    Producto(nombre="Medias de Compresión", descripcion="Compresión graduada para jornadas largas", tela="Nylon", precio_base=9500, activo=False, categoria_id=9)
]
session.add_all(productos)
session.commit()


# 3. Variantes (10 - talle, color y stock; hay una sin stock)
variantes = [
    Variante(sku="AMB-CLA-AZU-M", talle="M", color="Azul", stock=10, producto_id=1),
    Variante(sku="AMB-CLA-VER-L", talle="L", color="Verde", stock=8, producto_id=1),
    Variante(sku="AMB-JOG-NEG-S", talle="S", color="Negro", stock=6, producto_id=2),
    Variante(sku="CHA-TER-GRI-M", talle="M", color="Gris", stock=4, producto_id=3),
    Variante(sku="PAN-CAR-AZM-L", talle="L", color="Azul marino", stock=12, producto_id=4),
    Variante(sku="GUA-CLA-BLA-M", talle="M", color="Blanco", stock=7, producto_id=5),
    Variante(sku="GOR-QUI-FLO-U", talle="Único", color="Floral", stock=25, producto_id=6),
    Variante(sku="ZUE-ANT-BLA-39", talle="39", color="Blanco", stock=0, producto_id=7),
    Variante(sku="CAS-CUE-CEL-XL", talle="XL", color="Celeste", stock=5, producto_id=8),
    Variante(sku="BAR-TRI-CEL-U", talle="Único", color="Celeste", stock=40, producto_id=9)
]
session.add_all(variantes)
session.commit()


# 4. Clientes (10 - Variedad de particulares e instituciones)
clientes = [
    Cliente(nombre="Laura Benítez", tipo="particular", email="laura@mail.com", telefono="1155550101", direccion="Av. Corrientes 1234, CABA"),
    Cliente(nombre="Martín Suárez", tipo="particular", email="martin@mail.com", telefono="1155550102", direccion="Belgrano 456, Rosario"),
    Cliente(nombre="Clínica San Martín", tipo="institucion", email="compras@clinicasanmartin.com", telefono="1155550103", direccion="San Martín 800, La Plata"),
    Cliente(nombre="Valeria Ruiz", tipo="particular", email="valeria@mail.com", telefono="1155550104", direccion="Mitre 220, Córdoba"),
    Cliente(nombre="Hospital Italiano Sur", tipo="institucion", email="insumos@hisur.com", telefono="1155550105", direccion="Rivadavia 3000, CABA"),
    Cliente(nombre="Nicolás Herrera", tipo="particular", email="nicolas@mail.com", telefono="1155550106", direccion="Sarmiento 90, Mendoza"),
    Cliente(nombre="Florencia Molina", tipo="particular", email="flor@mail.com", telefono="1155550107", direccion="Urquiza 745, Tucumán"),
    Cliente(nombre="Sanatorio del Valle", tipo="institucion", email="admin@sanatoriovalle.com", telefono="1155550108", direccion="Ruta 9 km 12, Pilar"),
    Cliente(nombre="Joaquín Acosta", tipo="particular", email="joaquin@mail.com", telefono="1155550109", direccion="Lavalle 150, Mar del Plata"),
    Cliente(nombre="Centro Médico Norte", tipo="institucion", email="pedidos@cmnorte.com", telefono="1155550110", direccion="Libertador 5500, Vicente López")
]
session.add_all(clientes)
session.commit()


# 5. Pedidos (10 - distintos estados)
pedidos = [
    Pedido(fecha=date(2026, 9, 1), estado="entregado", total=70000, cliente_id=1),
    Pedido(fecha=date(2026, 9, 3), estado="entregado", total=35000, cliente_id=2),
    Pedido(fecha=date(2026, 9, 8), estado="pendiente", total=360000, cliente_id=3),
    Pedido(fecha=date(2026, 9, 10), estado="enviado", total=84000, cliente_id=4),
    Pedido(fecha=date(2026, 9, 14), estado="pendiente", total=250000, cliente_id=5),
    Pedido(fecha=date(2026, 9, 18), estado="entregado", total=22500, cliente_id=6),
    Pedido(fecha=date(2026, 9, 22), estado="cancelado", total=28000, cliente_id=7),
    Pedido(fecha=date(2026, 9, 25), estado="enviado", total=300000, cliente_id=8),
    Pedido(fecha=date(2026, 10, 2), estado="pendiente", total=24000, cliente_id=9),
    Pedido(fecha=date(2026, 10, 6), estado="entregado", total=420000, cliente_id=10)
]
session.add_all(pedidos)
session.commit()


# 6. Detalle de pedidos (10 - cantidad x precio_unitario = total del pedido)
detalles = [
    DetallePedido(cantidad=2, precio_unitario=35000, pedido_id=1, variante_id=1),
    DetallePedido(cantidad=1, precio_unitario=35000, pedido_id=2, variante_id=2),
    DetallePedido(cantidad=20, precio_unitario=18000, pedido_id=3, variante_id=5),
    DetallePedido(cantidad=2, precio_unitario=42000, pedido_id=4, variante_id=3),
    DetallePedido(cantidad=10, precio_unitario=25000, pedido_id=5, variante_id=6),
    DetallePedido(cantidad=5, precio_unitario=4500, pedido_id=6, variante_id=7),
    DetallePedido(cantidad=1, precio_unitario=28000, pedido_id=7, variante_id=4),
    DetallePedido(cantidad=15, precio_unitario=20000, pedido_id=8, variante_id=9),
    DetallePedido(cantidad=4, precio_unitario=6000, pedido_id=9, variante_id=10),
    DetallePedido(cantidad=12, precio_unitario=35000, pedido_id=10, variante_id=1)
]
session.add_all(detalles)
session.commit()
session.close()


print("¡Base de datos cargada con 10 registros por tabla!")