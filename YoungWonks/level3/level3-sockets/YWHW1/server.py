import socket


def encrypt(message, shift):
    encoded = []
    for letter in message:
        ascii = ord(letter) + int(shift)
        if ascii > 122:
            over = ascii - 122
            encoded.append(chr(96 + over))
        else:
            encoded.append(chr(ascii))
    
    return "".join(encoded)

def decrypt(message, shift):
    decoded = []
    for letter in message:
        ascii = ord(letter) - int(shift)
        if ascii < 97:
            under = 97 - ascii
            decoded.append(chr(123 - under))
        else:
            decoded.append(chr(ascii))

    return "".join(decoded)


s = socket.socket()

host = 'localhost'
port = 12345
s.bind((host, port))
s.listen(3)
conn, addr = s.accept()


listening = True
while listening:
    shift_input = input("Enter your shift: ").lower()
    message_input = input("Enter your message (type exit to exit): ").lower()
    if message_input.lower() == 'exit':
        listening = False
        to_send = 'exit'
    else:
        to_send = encrypt(message_input, shift_input) + ' | ' + shift_input
    
    if len(to_send) > 1024:
        print('Please send a message with under 1024 characters!')
        continue
    else:
        to_send = to_send + ' '*(1024 - len(to_send))
    
    encrypted_message = to_send.encode()
    conn.sendall(encrypted_message)
    print(f'You sent: {to_send.strip()}')
    
    if listening:
        received_data = conn.recv(1024)
        decoded_data = received_data.decode().strip()
        
        if decoded_data.lower() == 'exit':
            listening = False
        else:
            print(decoded_data)
            message, shift = decoded_data.split(' | ')
            
            guess = input("What is the decrypted message? ")
            if guess.lower() == decrypt(message, shift):
                print('Correct!')
            else:
                print('Incorrect!')

s.close()
conn.close()
