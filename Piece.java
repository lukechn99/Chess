public abstract class Piece {
	boolean isWhite;
	public abstract boolean move (int [] dest); // should be used to determine legality, not actual move
	public abstract boolean getIdentity ();
}