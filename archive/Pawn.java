public class Pawn extends Piece{
	int flocation, rlocation;
	boolean isWhite; // black pawns move down integers, white move up
	boolean moved = false;
	public Pawn (int f, int r, boolean b) {
		flocation = f;
		rlocation = r;
		isWhite = b;
	}
	public boolean getIdentity () {
		// returns true if white
		return isWhite;
	}
	public String toString () {
		if (isWhite) 
			return "| wP ";
		else
			return "| bP ";
	}
	public boolean move (int [] dest) {
		// should be used to determine legality, not actual move
		// look at first move 2 and 1 thereafter, param for moved or not
		if (((isWhite && dest[0] - flocation <= 2) || (!isWhite && flocation - dest[0] <= 2)) && moved == false) {
			moved = true;
			return true;
		}
		else
			moved = true;
			return false;
	} 
}