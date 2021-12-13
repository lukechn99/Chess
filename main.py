import chess
from search import *

def reporter(board):
  '''
  take a board and reports on what the outcome was
  '''
  message = "Game ended... "
  if board.is_checkmate(): message += "with checkmate, "
  if board.is_stalemate(): message += "with stalemate, "
  if board.is_insufficient_material(): message += "insufficient material, "
  if board.is_seventyfive_moves(): message += "seventyfive moves, "
  if board.is_fivefold_repetition(): message += "fivefold repetition, "
  if board.can_claim_fifty_moves(): message += "fifty moves, "
  if board.can_claim_threefold_repetition(): message += "threefold repetition, "
  if board.is_variant_win(): message += "some weird win, "
  if board.is_variant_loss(): message += "some weird loss, "
  if board.is_variant_draw(): message += "some weird draw, "
  print(message)

def play_self():
  board = chess.Board()
  e = CombinedEvaluator()
  turn = 0
  finished = False
  while not finished:
    print("move {}".format(turn))
    turn += 1
    print(board)
    if board.is_game_over():
      reporter(board)
      finished = True
      continue
    if board.is_check():
      print("check")
    print(list(board.legal_moves))
    move = abp(board, 50, e)
    print(move.uci())
    board.push(move)

def play_player():
  board = chess.Board()
  e = CombinedEvaluator()
  turn = 0
  finished = False
  while not finished:

    # computer turn
    print("move {}".format(turn))
    turn += 1
    if board.is_game_over():
      reporter(board)
      finished = True
      continue
    if board.is_check():
      print("check")
    move = abp(board, 50, e)
    print("Computer played {}".format(move.uci()))
    board.push(move)
    print(board)
    # player turn
    print("here are your available moves")
    print(board.legal_moves)
    player_move = input()
    board.push_san(player_move)
