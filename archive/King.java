public class King extends Piece{
	private int flocation, rlocation;
	private boolean isWhite; // black pawns move down integers, white move up
	public King (int f, int r, boolean b) {
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
			return "| wK ";
		else
			return "| bK ";
	}
	public boolean move (int [] dest) {
		// should be used to determine legality, not actual move
		return true;
	} 
}