import socket


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# La direccion ip y el `puerto
direccion_servidor = ('localhost', 8000)

# Conéctate al servidor
cliente.connect(direccion_servidor)

# Envíando los datos del lado servidor
mensaje = input("Ingrese los caracteres:")
cliente.sendall(mensaje.encode())

# Recibe la respuesta del servidor
datos = cliente.recv(1024).decode()
print(datos)

# Cerramos la conexion
cliente.close()
