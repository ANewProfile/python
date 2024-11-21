import socket


s = socket.socket()
host = '192.168.4.151'
port = 12345

s.connect((host, port))


running = True
while running:
    received_data = s.recv(1024)
    decoded_data = received_data.decode().strip()
    if decoded_data.lower() == 'exit':
        running = False
    else:
        print(decoded_data)
        
        user_input = input("Enter your message: ")
        if user_input.lower() == 'exit':
            running = False
        if len(user_input) > 1024:
            user_input = user_input[:1024]
        else:
            user_input = user_input + ' '*(1024 - len(user_input))
            
        encoded_input = user_input.encode()
        
        s.sendall(encoded_input)
        print(f'You sent: {user_input.strip()}')

s.close()
