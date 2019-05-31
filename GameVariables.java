public class GameVariables {
	private boolean whiteCheck = false;
	private boolean blackCheck = false;
	private int whitePoints = 0;
	private int blackPoints = 0;
	public int getPoints (String p) {
		if (p == white)
			return whitePoints;
		else 
			return blackPoints;
	}
	public void setWhitePoints (int i) {
		whitePoints += i;
	}
	public void setBlackPoints (int i) {
		blackPoints += i;
	}
	public boolean isInCheck (String p) {
		if (p == white)
			return whiteCheck;
		else 
			return blackCheck;
	}
	public void whiteCheck (boolean b) {
		
	}
}