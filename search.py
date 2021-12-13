import chess
from evaluator import *
from copy import deepcopy

def bfs(board, depth):
  '''
  given a board, finds the next best possible move considering a certain depth
  '''
  #keep in mind that board.legal_moves works for both sides. Once you push a 
  #move for white, board.legal_moves show legal moves for black to make and so on.
  e = CombinedEvaluator()

  def explore(board, depth):
    if depth == 0:
      return e.evaluate(board)
    possible_boards = []
    for move in board.legal_moves:
      board_instance = deepcopy(board)
      board_instance.push(move)
      possible_boards.append(explore(board_instance, depth - 1))
    if possible_boards:
      return e.evaluate(board) + sorted(possible_boards)[-1]      # not sure why, but sometimes there is no possible move
    else:
      return e.evaluate(board)
  
  possible_boards = []
  for move in board.legal_moves:
    board_instance = deepcopy(board)
    board_instance.push(move)
    possible_boards.append((explore(board_instance, depth), move))
  result = sorted(possible_boards, key=lambda tup: tup[0])
  return result