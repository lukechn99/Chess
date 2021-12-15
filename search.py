import chess
from evaluator import *
from copy import deepcopy

def abp(board, depth, e):
  '''
  given a board, finds the next best move through alpha-beta pruning

  pseudocode
  if node is a leaf
    return the utility value of node
  if node is a minimizing node
    for each child of node
        beta = min (beta, abp (child, alpha, beta))
        if beta <= alpha
            return beta
        return beta
  if node is a maximizing node
    for each child of node
        alpha = max (alpha, abp (child, alpha, beta))
        if beta <= alpha
            return alpha
        return alpha
  '''
  def explore(board, depth, e, alpha, beta):
    if not list(board.legal_moves) or depth == 0:
      return e.evaluate(board)
    if board.turn:      # white's turn, maximize
      for move in board.legal_moves:
        board_instance = deepcopy(board)
        board_instance.push(move)
        beta = min(beta, explore(board_instance, depth - 1, e, alpha, beta))
        if beta <= alpha:
          return beta
        return beta
    else:               # black's turn, minimize
      for move in board.legal_moves:
        board_instance = deepcopy(board)
        board_instance.push(move)
        alpha = max(alpha, explore(board_instance, depth - 1, e, alpha, beta))
        if beta <= alpha:
          return alpha
        return alpha

  possible_boards = []
  for move in board.legal_moves:
    board_instance = deepcopy(board)
    board_instance.push(move)
    possible_boards.append((explore(board_instance, depth, e, float('-inf'), float('inf')), move))
  return sorted(possible_boards, key=lambda tup: tup[0])[-1][1]

def bfs(board, depth, e):
  '''
  given a board, finds the next best possible move considering a certain depth
  '''
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
  result = sorted(possible_boards, key=lambda tup: tup[0])[-1][1]
  return result

def bfs_with_horizon(board, depth, e):
  '''
  given a board, examines all possible moves at a shallow depth and then explores
  the best moves at a deeper depth
  '''
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

  # preliminary eval with depth of 1
  possible_boards = []
  for move in board.legal_moves:
    board_instance = deepcopy(board)
    board_instance.push(move)
    possible_boards.append((explore(board_instance, 2), move))
  
  deeper_exploration = sorted(possible_boards[:5], key=lambda tup: tup[0])
  final_boards = []
  for move in deeper_exploration:
    move = move[1]
    board_instance = deepcopy(board)
    board_instance.push(move)
    final_boards.append((explore(board_instance, depth), move))

  result = sorted(final_boards, key=lambda tup: tup[0])[-1][1]
  return result