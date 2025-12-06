import socket

# Server configuration
HOST = "0.0.0.0"
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server is listening...')
    
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            message = input("Type 'STOP' to terminate the client program, or anything else to continue: ")
            if message.upper() == 'STOP':
                conn.sendall(b'STOP')
                print("STOP signal sent to the client.")
                break
            else:
                print("No stop signal sent. Client continues running.")
