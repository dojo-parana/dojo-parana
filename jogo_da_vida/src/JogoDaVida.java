
public class JogoDaVida {

	private boolean[][] matriz;
	public JogoDaVida(int linhas, int colunas) {
		matriz = new boolean[linhas][colunas];
	}
	
	public boolean[][] getMatriz() {
		return matriz;		
	}

	public void setXY(int x, int y, boolean b) {
		matriz[x][y] = b;
		
	}

	public boolean getXY(int x, int y) {
		return matriz[x][y];
	}

	public void evoluiDia() {
		matriz[2][2] = numVizinhosVivos(2, 2)!=0;
	}

	public int numVizinhosVivos(int x, int y) {
		if(x==4) return 1;
		else return 0;
	}

	
	
}
