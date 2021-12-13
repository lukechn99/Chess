import chess
from copy import deepcopy

class Evaluator:
  def __init__(self):
    self.piecevalues = {"P": 1, "N": 3, "B": 3, "R": 4, "Q": 9, "K": 38, 
                        "p": -1, "n": -3, "b": -3, "r": -4, "q": -9, "k": -38}
    # piece_square_tables is a commonly used positional evaluation method 
    # inspired by https://www.chessprogramming.org/Simplified_Evaluation_Function
    self.piece_square_tables = {
        "P": [[0,  0,  0,  0,  0,  0,  0,  0],
              [50, 50, 50, 50, 50, 50, 50, 50],
              [10, 10, 20, 30, 30, 20, 10, 10],
              [5,  5, 10, 25, 25, 10,  5,  5],
              [0,  0,  0, 20, 20,  0,  0,  0],
              [5, -5,-10,  0,  0,-10, -5,  5],
              [5, 10, 10,-20,-20, 10, 10,  5],
              [0,  0,  0,  0,  0,  0,  0,  0]],
        "N": [[-50,-40,-30,-30,-30,-30,-40,-50],
              [-40,-20,  0,  0,  0,  0,-20,-40],
              [-30,  0, 10, 15, 15, 10,  0,-30],
              [-30,  5, 15, 20, 20, 15,  5,-30],
              [-30,  0, 15, 20, 20, 15,  0,-30],
              [-30,  5, 10, 15, 15, 10,  5,-30],
              [-40,-20,  0,  5,  5,  0,-20,-40],
              [-50,-40,-30,-30,-30,-30,-40,-50]], 
        "B": [[-20,-10,-10,-10,-10,-10,-10,-20],
              [-10,  0,  0,  0,  0,  0,  0,-10],
              [-10,  0,  5, 10, 10,  5,  0,-10],
              [-10,  5,  5, 10, 10,  5,  5,-10],
              [-10,  0, 10, 10, 10, 10,  0,-10],
              [-10, 10, 10, 10, 10, 10, 10,-10],
              [-10,  5,  0,  0,  0,  0,  5,-10],
              [-20,-10,-10,-10,-10,-10,-10,-20]], 
        "R": [[0,  0,  0,  0,  0,  0,  0,  0],
              [5, 10, 10, 10, 10, 10, 10,  5],
              [-5,  0,  0,  0,  0,  0,  0, -5],
              [-5,  0,  0,  0,  0,  0,  0, -5],
              [-5,  0,  0,  0,  0,  0,  0, -5],
              [-5,  0,  0,  0,  0,  0,  0, -5],
              [-5,  0,  0,  0,  0,  0,  0, -5],
              [0,  0,  0,  5,  5,  0,  0,  0]],
        "Q": [[-20,-10,-10, -5, -5,-10,-10,-20],
              [-10,  0,  0,  0,  0,  0,  0,-10],
              [-10,  0,  5,  5,  5,  5,  0,-10],
              [-5,  0,  5,  5,  5,  5,  0, -5],
              [0,  0,  5,  5,  5,  5,  0, -5],
              [-10,  5,  5,  5,  5,  5,  0,-10],
              [-10,  0,  5,  0,  0,  0,  0,-10],
              [-20,-10,-10, -5, -5,-10,-10,-20]],
        "K": [[-30,-40,-40,-50,-50,-40,-40,-30],
              [-30,-40,-40,-50,-50,-40,-40,-30],
              [-30,-40,-40,-50,-50,-40,-40,-30],
              [-30,-40,-40,-50,-50,-40,-40,-30],
              [-20,-30,-30,-40,-40,-30,-30,-20],
              [-10,-20,-20,-20,-20,-20,-20,-10],
              [20, 20,  0,  0,  0,  0, 20, 20],
              [20, 30, 10,  0,  0, 10, 30, 20]]
    }
    black_pieces = ["p", "n", "b", "r", "q", "k"]
    for piece in black_pieces:
      white_piece_square_table = self.piece_square_tables[piece.upper()]
      black_piece_square_table = []
      for row in range(len(white_piece_square_table)-1, -1, -1):
        black_row = []
        for i in range(len(white_piece_square_table[0])-1, -1, -1):
          black_row.append(white_piece_square_table[row][i] * -1)
        black_piece_square_table.append(black_row)
      self.piece_square_tables[piece] = black_piece_square_table

    # the values given by established chess tables seem too high, dampening
    # will take the influence of position down a notch
    self.piece_square_tables_dampening = 0.01

  def evaluate(self, board):
    '''
    given a board, returns the signed float value of the board
    '''
    return 0

class CheckOpportunityEvaluator(Evaluator):
  '''
  Gives some weight towards putting the opponent in check and gives huge value 
  to putting opponent in checkmate
  '''
  def __init__(self):
    super().__init__()

  def evaluate(self, board):
    board_value = 0
    for move in board.legal_moves:
      board_instance = deepcopy(board)
      board_instance.push(move)
      if board.is_check:
        board_value += 1 if board.turn else -1
      elif board.is_checkmate:
        board_value += float('inf') if board.turn else float('-inf') 
    return board_value

class CaptureEvaluator(Evaluator):
  '''
  Evaluates purely on material able to be captured on the current turn
  '''
  def __init__(self):
    super().__init__()

  def evaluate(self, board):
    board_value = 0
    for move in board.legal_moves:
      if board.is_capture(move):                              # if a capture is possible, search up what piece would be captured
        captured = board.remove_piece_at(move.to_square)      # removes and returns piece
        if captured:
          value = self.piecevalues[captured.symbol()] * -0.1    # record what the piece is and alter board_value
          board_value += value
        board.set_piece_at(move.to_square, captured)          # replace piece back in its place
    return board_value

class PointwiseEvaluator(Evaluator):
  '''
  Evaluates purely on board material during the current turn
  '''
  def __init__(self):
    super().__init__()

  def evaluate(self, board):
    board_value = 0
    for pos in board.board_fen():
      if pos.isalpha():
        board_value += self.piecevalues[pos]
    return board_value

class PositionalEvaluator(Evaluator):
  '''
  Evaluates based on what chess players commonly agree upon as positionally
  advantageous. 
  Advantages include passed pawns, knights towards the center, bishops toward
  central diagonals, bishop pairs, etc.
  '''
  def __init__(self):
    super().__init__()

  def evaluate(self, board):
    board_value = 0
    board_rows = board.board_fen().split("/")
    for r, row in enumerate(board_rows):
      c = 0
      for pos in row:
        if pos.isdigit():
          c += int(pos)
        else:
          # determine piece and value
          piece_value = self.piecevalues[pos]
          positional_weight = self.piece_square_tables[pos][r][c] * self.piece_square_tables_dampening * 1 if board.turn else -1
          board_value += piece_value * positional_weight
          c += 1

    return board_value

class CombinedEvaluator(Evaluator):
  def __init__(self):
    super().__init__()
    self.evaluators = [CaptureEvaluator(), PointwiseEvaluator(), PositionalEvaluator(), CheckOpportunityEvaluator()]
    self.evaluator_weights = [0.5, 1.5, 0.1, 2]

  def _sigmoid_standardization(self, value):
    '''
    constrains a evaluation to a sigmoid for more even comparison
    '''
    return 1 / (1 + math.exp(-value))

  def evaluate(self, board):
    board_value = 0
    for i, e in enumerate(self.evaluators):
      board_value += self._sigmoid_standardization(e.evaluate(board)) * self.evaluator_weights[i]
    return board_value