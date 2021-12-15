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

def play_self(e=EnsembleEvaluator()):
  board = chess.Board()
  turn = 0
  finished = False
  while not finished:# and turn < 100:
    # print("move {}".format(turn))
    turn += 1
    # print(board)
    if board.is_game_over():
      # reporter(board)
      finished = True
      continue
    # print(list(board.legal_moves))
    move = abp(board, 20, e)
    # print(move.uci())
    board.push(move)
  return board

def play_player(e=EnsembleEvaluator()):
  board = chess.Board()
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
    move = abp(board, 50, e)
    print("Computer played {}".format(move.uci()))
    board.push(move)
    print(board)
    # player turn
    print("here are your available moves")
    print(board.legal_moves)
    player_move = input()
    board.push_san(player_move)
  return board

'''
Playing against stockfish requires you to install stockfish, please look up the documentation online
'''
# from stockfish import Stockfish

# def play_stockfish(elo):
#   board = chess.Board()
#   e = CombinedEvaluator()
#   stockfish = Stockfish("/usr/local/lib/python3.7/dist-packages/stockfish/")
#   stockfish.set_elo_rating(1350)

#   turn = 0
#   finished = False
#   while not finished:
#     # computer turn
#     turn += 1
#     if board.is_game_over():
#       reporter(board)
#       finished = True
#       continue
#     move = abp(board, 50, e)
#     board.push(move)
#     # stockfish move
#     stockfish.set_fen_position(board.fen())
#     stockfish_move = stockfish.get_best_move()
#     board.push_san(stockfish_move)