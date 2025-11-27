import uuid

class Usuario:

    def __init__(self, nombre: str, email: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email

    def is_admin(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} ({self.email})"


class Cliente(Usuario):
    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)
        self.direccion = direccion

    def __str__(self) -> str:
        return f"[{self.id}] Cliente: {self.nombre} ({self.email}), Dirección: {self.direccion}"


class Administrador(Usuario):
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[{self.id}] Administrador: {self.nombre} ({self.email})"