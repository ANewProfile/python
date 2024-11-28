import game
import socket


s = socket.socket()

host = 'localhost'
port = 12345

s.connect((host, port))

turn = 1
won = False
while not won:
    turn += 1
    turn = turn % 2
    
    game.display(game.board)
    if turn == 1:
        move = input("Where would you like to go? ")
        message = move.encode()
        s.sendall(message)
    else:
        received_data = s.recv(1)
        move = received_data.decode()
    
    game.board = game.move(game.board, int(move), turn)
    game.display(game.board)
    
    if game.check_board(game.board):
        won = True

s.close()
