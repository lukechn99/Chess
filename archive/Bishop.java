public class Bishop extends Piece{
	int flocation, rlocation;
	boolean isWhite; // black pawns move down integers, white move up
	public Bishop (int f, int r, boolean b) {
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
			return "| wB ";
		else
			return "| bB ";
	}
	public boolean move (int [] dest) {return true;} // should be used to determine legality, not actual move
}