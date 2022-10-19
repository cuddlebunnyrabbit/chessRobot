import chess

board = chess.Board()

board.legal_moves
chess.Move.from_uci("a8a1") in board.legal_moves

board.push_san("e4")
print(board)
board.push_san("d5")
print(board)
board.push_san("exd5")
print(board)
board.push_san("c6")
print(board)
board.push_san("dxc6")
print(board)
board.push_san("h6")
print(board)
board.push_san("cxb7")
print(board)
board.push_san("Kd7")
print(board)
board.push_san("bxc8=Q")
print(board)


'''
board.is_checkmate()
board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
'''
print(board)
