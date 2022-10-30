import chess
import chess.pgn
'''
game = chess.pgn.Game()
game.headers["Event"] = "Example"

node = None
print(node)

def log_move(move):
    node = 1
    print

    if node == None:
        node = game.add_variation(chess.Board.push(move))
    else:
        node = node.add_variation(chess.Board.push(move))

    print(game)

log_move("e4")
log_move("e5")
'''

board = chess.Board()
game = chess.pgn.Game()

board.legal_moves
chess.Move.from_uci("a8a1") in board.legal_moves


game.headers["Event"] = "Example"
node = game.add_variation(board.push("e4"))
node = node.add_variation(board.push("d5"))
node = node.add_variation(board.push("exd5"))