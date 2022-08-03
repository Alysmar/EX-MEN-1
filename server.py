import socket   
import threading
import gc
import sys


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Servidor corriendo en {host}:{port}")


clients = []
usuarios = []

def transmitir(msj, _client):
    for client in clients:
        if client != _client:
            client.send(msj)

def manejador_msj(client):
    while True:
        try:
            msj = client.recv(1024)
            transmitir(msj, client)
        except:
            index = clients.index(client)
            usuario = usuarios[index]
            transmitir(f"ChatBot: {usuario} se ha desconectado".encode('utf-8'), client)
            clients.remove(client)
            usuarios.remove(usuario)
            client.close()
            print(f" {usuario} se ha desconectado")
            
            # implementando garbage collector
            print("recuento de referencias del objeto:",gc.get_count())
            collected= gc.collect()
            print("Garbage collector: collected", "%d objects." % collected)
            print("recuento de referencias del objeto:",gc.get_count())
            break


def conexiones():
    while True:
        client, address = server.accept()
        client.send("@usuario".encode("utf-8"))
        usuario = client.recv(1024).decode('utf-8')
        clients.append(client)
        usuarios.append(usuario)
        print(f"{usuario} esta conectado {str(address)}")
        msj = f"ChatBot: {usuario} se ha unido al chat!".encode("utf-8")
        transmitir(msj, client)
        client.send("Conectado al servidor".encode("utf-8"))
        thread = threading.Thread(target=manejador_msj, args=(client,))
        thread.start()
        

try:
    
        print("Umbrales de recolección de basura:", gc.get_threshold())
        print("recuento de referencias del objeto:",gc.get_count())
        collected= gc.collect()
        print("Garbage collector: collected", "%d objects." % collected)
        print("recuento de referencias del objeto:",gc.get_count())
        conexiones()

except KeyboardInterrupt:
#interrumpimos la conexion con crtl+ c  
    sys.exit(0)