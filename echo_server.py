import socket

ip='127.0.0.1'
port=5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen()
    connection, address = server.accept()

    with connection:
        print('Connected :: ' , address)
        msg = ''
        while True:
            data = connection.recv(1024)

            if data:
                msg += data.decode('utf-8')
                
                if data.decode('utf-8') == '\r\n' or data.decode('utf-8').endswith('\r\n'):
                    print(msg)
                    connection.send(bytes('msg :: ' + msg, 'utf-8'))

                    if msg == 'quit\r\n':
                        connection.shutdown(1)
                        connection.close()
                        break
                    msg = ''

            

