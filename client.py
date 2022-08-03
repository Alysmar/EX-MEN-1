import socket   
import threading

usuario = input("Ingresa nombre de usuario: ")

host = '127.0.0.1'
port = 55555

def recibir_msj():
    while True:
        try:
            msj = client.recv(1024).decode('utf-8')

            if msj == "@usuario":
                client.send(usuario.encode("utf-8"))
            else:
                print(msj)
        except:
            print("No se ha podido establecer conexion con el servidor")
            client.close
            break

def escribir_msj():
    while True:
        msj = f"{usuario}: {input('')}"
        client.send(msj.encode('utf-8'))

try:        
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))    
    receive_thread = threading.Thread(target=recibir_msj)
    receive_thread.start()

    write_thread = threading.Thread(target=escribir_msj)
    write_thread.start()

except:
        print("\nno se pudo conectar al servidor")      



