public class Rook extends Piece {
	int flocation, rlocation;
	boolean isWhite;
	public Rook (int f, int r, boolean b) {
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
			return "| wR ";
		else
			return "| bR ";
	}
	public boolean move (int [] dest) {return true;} // should be used to determine legality, not actual move
}