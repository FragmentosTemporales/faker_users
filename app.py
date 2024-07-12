from faker_user import FakeUser

def crear_usuarios(n):
    usuarios = [FakeUser().mostrar_usuario() for _ in range(n)]
    return usuarios

if __name__=='__main__':
    usuarios = crear_usuarios(10)
    print(usuarios)