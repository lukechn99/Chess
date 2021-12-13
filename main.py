import chess
from search import *

board = chess.Board()
turn = 0
finished = False
while not finished:
  print("move {}".format(turn))
  turn += 1
  print(board)
  if board.is_game_over():
    print("gameover")
    finished = True
    continue
  print(list(board.legal_moves))
  move = bfs(board, 2)[-1][1]
  print(move.uci())
  board.push(move)
