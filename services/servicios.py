from typing import Dict, List
from models.usuario import Usuario, Cliente, Administrador
from models.producto import Producto
from models.pedido import Pedido

class TiendaService:

    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    # -------------------------
    # Usuarios
    # -------------------------
    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: str = "") -> Usuario:
        if tipo == "cliente":
            usuario = Cliente(nombre, email, direccion)
        elif tipo == "admin":
            usuario = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido")
        self.usuarios[usuario.id] = usuario
        return usuario

    # -------------------------
    # Productos
    # -------------------------
    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> None:
        if producto_id in self.productos:
            del self.productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    # -------------------------
    # Pedidos
    # -------------------------
    def realizar_pedido(self, cliente_id: str, items: Dict[str, int]) -> Pedido:
        if cliente_id not in self.usuarios or not isinstance(self.usuarios[cliente_id], Cliente):
            raise ValueError("Cliente no válido")

        cliente = self.usuarios[cliente_id]
        productos_pedido: Dict[Producto, int] = {}

        for prod_id, cantidad in items.items():
            if prod_id not in self.productos:
                raise ValueError(f"Producto {prod_id} no encontrado")
            producto = self.productos[prod_id]
            if not producto.hay_stock(cantidad):
                raise ValueError(f"Stock insuficiente para {producto.nombre}")
            productos_pedido[producto] = cantidad

        # Descontar stock
        for prod, cantidad in productos_pedido.items():
            prod.actualizar_stock(-cantidad)

        pedido = Pedido(cliente, productos_pedido)
        self.pedidos.append(pedido)
        return pedido

    def pedidos_por_usuario(self, cliente_id: str) -> List[Pedido]:
        return [p for p in self.pedidos if p.cliente.id == cliente_id]
