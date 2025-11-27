
from models.producto import ProductoElectronico, ProductoRopa
from services.tienda_servicios import TiendaService

def main():  # Tienda
    tienda = TiendaService()

    # Registro usuarios
    cliente1 = tienda.registrar_usuario("cliente", "Marcos", "mmc1508@mail.com", "Calle 1")
    cliente2 = tienda.registrar_usuario("cliente", "David", "dymcmail.com", "Calle 2")
    cliente3 = tienda.registrar_usuario("cliente", "Anton", "tony@mail.com", "Calle 3")
    admin = tienda.registrar_usuario("admin", "Admin", "admin@mail.com")

    # Creacion productos
    p1 = ProductoElectronico("Laptop", 1000.0, 5, 24)
    p2 = ProductoElectronico("Smartphone", 600.0, 10, 12)
    p3 = ProductoRopa("Camiseta", 20.0, 50, "M", "Azul")
    p4 = ProductoRopa("Pantalón", 35.0, 40, "L", "Negro")
    p5 = ProductoRopa("Sudadera", 50.0, 30, "XL", "Rojo")

    # Añador productos al inventario
    for producto in [p1, p2, p3, p4, p5]:
        tienda.agregar_producto(producto)

    # 5Listar productos
    print("\n=== INVENTARIO ===")
    for prod in tienda.listar_productos():
        print(prod)

    # Simular pedidos
    print("\n=== PEDIDOS ===")
    pedido1 = tienda.realizar_pedido(cliente1.id, {p1.id: 1, p3.id: 2})
    pedido2 = tienda.realizar_pedido(cliente2.id, {p2.id: 1, p4.id: 1})
    pedido3 = tienda.realizar_pedido(cliente1.id, {p5.id: 3})

    print("\nPedido 1:\n", pedido1)
    print("\nPedido 2:\n", pedido2)
    print("\nPedido 3:\n", pedido3)

    # Pedidos de un cliente
    print(f"\n=== HISTÓRICO DE PEDIDOS DE {cliente1.nombre} ===")
    for pedido in tienda.pedidos_por_usuario(cliente1.id):
        print(pedido, "\n")

    # Stock actualizado
    print("\n=== STOCK ACTUALIZADO ===")
    for prod in tienda.listar_productos():
        print(prod)

if __name__ == "__main__":
    main()
