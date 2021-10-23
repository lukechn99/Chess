import java.util.Scanner;
public class Main {
	public static Piece [][] board = new Piece[8][8];
	public static int whitePts = 0;
	public static int blackPts = 0;
	public static boolean blackCheck = false;
	public static boolean whiteCheck = false;
	public static String moves = "";
	// in order to determine checks, do you need to store all possible moves?
	// No, only if the most recent move attacks the king, but what about discovered checks?
	public static void displayForWhite (Piece [][] board) {
		System.out.println("     WHITE MOVE");
		System.out.println("     _______________________________________");
		for (int i = 0; i < 8; i++) {
			System.out.print(" " + (8 - i) + "  ");
			for (int j = 0; j < 8; j++) {
				if (board[i][j] == null)
					System.out.print("|    ");
				else
					System.out.print(board[i][j]);
			}
			System.out.print("|");
			System.out.print("\n" + "    |____|____|____|____|____|____|____|____|" + "\n");
		}
		System.out.println("\n" + "      a    b    c    d    e    f    g    h");
	}
	public static void displayForBlack (Piece [][] board) {
		System.out.println("     BLACK MOVE");
		System.out.println("     _______________________________________");
		for (int i = 7; i >= 0; i--) {
			System.out.print(" " + (8 - i) + "  ");
			for (int j = 7; j >= 0; j--) {
				if (board[i][j] == null)
					System.out.print("|    ");
				else
					System.out.print(board[i][j]);
			}
			System.out.print("|");
			System.out.print("\n" + "    |____|____|____|____|____|____|____|____|" + "\n");
		}
		System.out.println("\n" + "      h    g    f    e    d    c    b    a");
	}
	public static int letterToNumber(char c) {
		int n = (int) c - 97;
		return n;
	}
	public static int [] selectHelper(String coord) { 
		// takes in strings "a1" "c7" converts to char arr then to coordinates [0, 0, 2, 6]
		char [] s = coord.toCharArray();
		int [] output = new int[2];
		output[1] = letterToNumber(s[0]);
		output[0] = 8 - (s[1] - 48);
		return output;
	}

	public static void main (String [] args) { 
		// build a chess clock?
		// how to castle? en passant? promote? determine checkmate?

		//generate pieces
		for (int i = 0; i < 8; i++) {board[1][i] = new Pawn(1, i, false);}
		for (int i = 0; i < 8; i++) {board[6][i] = new Pawn(6, i, true);}

		board[0][0] = new Rook(0, 0, false);
		board[0][7] = new Rook(0, 7, false);
		board[7][0] = new Rook(7, 0, true);
		board[7][7] = new Rook(7, 7, true);

		board[0][1] = new Knight(0, 1, false);
		board[0][6] = new Knight(0, 6, false);
		board[7][1] = new Knight(7, 1, true);
		board[7][6] = new Knight(7, 6, true);

		board[0][2] = new Bishop(0, 2, false);
		board[0][5] = new Bishop(0, 5, false);
		board[7][2] = new Bishop(7, 2, true);
		board[7][5] = new Bishop(7, 5, true);

		board[0][4] = new King(0, 4, false);
		board[0][3] = new Queen(0, 3, false);
		board[7][4] = new King(7, 4, true);
		board[7][3] = new Queen(7, 3, true);

		// test boards
		//displayForWhite(board);
		//displayForBlack(board);

		//use linked list to save moves? When ending game can save game
		Scanner s = new Scanner(System.in);
		boolean whiteTurn = true;
		boolean gameOn = true; // false exits while loop

		while (gameOn) {
			// display player board
			if (whiteTurn) {displayForWhite(board);}
			else {displayForBlack(board);}

			boolean pieceSelected = false;
			boolean illegalMove = true;
			int [] startCoord, destCoord;

			while (!pieceSelected) {
				// allow user to select a piece
				System.out.println("Select a piece: ");
				String start = s.next();
				startCoord = selectHelper(start);

				//Check to make sure the piece selected exists and is the right color
				while (illegalMove) {
					if (board[startCoord[0]][startCoord[1]] != null) { // && Piece.getIdentity(board[startCoord[0]][startCoord[1]]) == whiteTurn
						Piece selected = board[startCoord[0]][startCoord[1]];
						pieceSelected = true;
						System.out.println("Selected " + selected);
						System.out.println("Select destination: ");
						String dest = s.next();
						destCoord = selectHelper(dest);
						if (board[startCoord[0]][startCoord[1]].move(destCoord)) {
							// if legal destination
							board[destCoord[0]][destCoord[1]] = selected;
							board[startCoord[0]][startCoord[1]] = null;
							moves += start + " to " + dest;
							illegalMove = false;
						}
						else {
							System.out.println("Illegal move");
							/*Thread.sleep(1000); 
							System.out.print("\b\b\b\b\b\b\b\b\b\b\b\b");*/
						}
					}
				}
			}
			




			/*if (board[rStart][cStart] != null) {
				if (Main.board[rStart][cStart] instanceof Pawn)
					Pawn.move(rStart, cStart, rDest, cDest);
			}
			else
				System.out.println("no piece there");
			*/

			// next player's turn
			if (whiteTurn) {whiteTurn = false;}
			else {whiteTurn = true;}
			// if checkmate then gameOn = false
		}
		System.out.println(moves);
	}
}