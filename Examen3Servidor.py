import socket
from datetime import datetime



servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# la direecion y el puerto en el que sera escuchado
direccion = ('localhost', 8000)
servidor.bind(direccion)

# Espera conexiones entrantes
servidor.listen()

print(f"Servidor escuchando en {direccion}")

def cadena(cad):
    pais = ""
    edad = ""
    gen = ""
    fechanacimiento = ""
    nombre = ""
    
    if len(cad) >= 22:
        pais = cad[0:2]
        edad = int(cad[2:4])
        gen = cad[4]
        fechanacimiento = datetime.strptime(cad[5:13], '%Y%m%d')
        nombre = cad[13:]
        
        
        # País
        if pais == "01":
            pais_str = "Honduras"
        elif pais == "02":
            pais_str = "Costa Rica"
        elif pais == "03":
            pais_str = "México"
        else:
            pais_str = "país desconocido"
        
        # Género
        if gen == "F":
            genero_str = "femenino"
        elif gen == "M":
            genero_str = "masculino"
        else:
            genero_str = "género desconocido"

             # Edad
        if edad >= 1 and edad <= 18:
            edad_str = "menor de edad"
        elif edad >= 19 and edad <= 50:
            edad_str = "adulto"
        elif edad >= 51:
            edad_str = "tercera edad"
        else:
            edad_str = "edad desconocida"
        
      
        fechaactual = datetime.now()
        edadcalculada = fechaactual.year - fechanacimiento.year - ((fechaactual.month, fechaactual.day) < (fechanacimiento.month, fechanacimiento.day))

        if edadcalculada == edad:
                edadrespuesta = f"Hola {nombre} veo que eres del país de {pais_str}, tienes una edad de {edad} años. Por los datos enviados me indica que eres {edad_str}, y tu género es {genero_str}."
        else:
            edadrespuesta = f"Hola {nombre} veo que eres del país de {pais_str}, tienes una edad de {edad} años. Por los datos enviados me indica que eres {edad_str}, y tu género es {genero_str}. Pero viendo tu fecha de nacimiento ({fechanacimiento.strftime('%Y-%m-%d')}) la edad tuya no concuerda con tu fecha de nacimiento."
        
        return edadrespuesta
    
    return "Se han registrrado caracteres invalidos"

while True:
    # Acepta la conexión entrante
    conexion, direccion_cliente = servidor.accept()
    print(f"Conexión establecida con  {direccion_cliente}")

    # Muestra los datos recibidos por el cliente
    datos = conexion.recv(1024).decode('utf-8')
    print("Recibimos del lado cliente", datos)

    # Muestra la respuesta al cliente
    mensaje = cadena(datos)
    conexion.sendall(mensaje.encode('utf-8'))

    # Cerramos la conexion
    conexion.close()
