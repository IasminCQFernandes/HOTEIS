import socket

def get_host_name():
    return socket.gethostname()

host_name = get_host_name()
print(host_name)