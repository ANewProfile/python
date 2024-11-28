import game
import socket


s = socket.socket()
host = 'localhost'
port = 12345

s.bind((host, port))
s.listen(5)

conn, addr = s.accept()

turn = 1
won = False
while not won:
    turn += 1
    turn = turn % 2
    
    if turn == 0:
        move = input("Where would you like to go? ")
        message = move.encode()
        conn.sendall(message)
    else:
        received_data = conn.recv(1)
        move = received_data.decode()
    
    game.board = game.move(game.board, int(move), turn)
    game.display(game.board)
    
    if game.check_board(game.board):
        won = True

conn.close()
s.close()
