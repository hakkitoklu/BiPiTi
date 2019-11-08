import socket,ssl

def certificateInformation(target):
    try:
        context = ssl.create_default_context()
        server = context.wrap_socket(socket.socket(), server_hostname=target)
        server.connect((target, 443))
        certificate = server.getpeercert()
        print("[+]Certificate Serial Number: ", certificate.get('serialNumber'))
        print("[+]Certificate SSL Version:", certificate.get('version'))
        print("[+]Certificate:", certificate)
    except:
        pass