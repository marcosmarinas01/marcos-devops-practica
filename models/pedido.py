import uuid
from datetime import datetime
from typing import Dict
from models.usuario import Cliente
from models.producto import Producto

class Pedido:

    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]):
        self.id = str(uuid.uuid4())
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = productos  

    def calcular_total(self) -> float:
        return sum(prod.precio * cant for prod, cant in self.productos.items())

    def __str__(self) -> str:
        productos_str = "\n".join(
            [f" - {prod.nombre} x{cant} = {prod.precio * cant}€"
             for prod, cant in self.productos.items()]
        )
        return (
            f"Pedido {self.id} ({self.fecha.strftime('%Y-%m-%d %H:%M')})\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Productos:\n{productos_str}\n"
            f"Total: {self.calcular_total()}€"
        )
 