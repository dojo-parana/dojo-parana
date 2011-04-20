import com.sun.org.apache.bcel.internal.generic.INSTANCEOF;

import junit.framework.TestCase;


public class TestJogoDaVida extends TestCase {

	JogoDaVida jogo = null;
	final static int LINHAS = 5;
	final static int COLUNAS = 5;
	
	protected void setUp() throws Exception {
		super.setUp();
		jogo = new JogoDaVida(LINHAS, COLUNAS);
				
	}
	
	public void testVerificaMatriz () {
		assertTrue(jogo.getMatriz() instanceof boolean[][]);
	}

	public void testSetPosicaoXY() {
		jogo.setXY(2,2,true);
		assertTrue(jogo.getXY(2,2));
	}

	public void testMatrizMorta() {
		
		for(int i=0;i<LINHAS;i++)
			for(int j=0;j<COLUNAS;j++)
				assertFalse(jogo.getXY(i, j));
	}
	
	public void testMatrizMortaEvolui(){
		jogo.evoluiDia();
		
		for(int i=0;i<LINHAS;i++)
			for(int j=0;j<COLUNAS;j++)
				assertFalse(jogo.getXY(i, j));
		
	}
	public void testCelulaIsolada(){
		jogo.setXY(2,2,true);
		jogo.evoluiDia();
		
		for(int i=0;i<LINHAS;i++)
			for(int j=0;j<COLUNAS;j++)
				assertFalse(jogo.getXY(i, j));
	}
	
	public void testCelulaEstaIsolada() {
		assertEquals(jogo.numVizinhosVivos(3,3),0);
	}

	public void testCelulaNaoEstaIsolada() {
		jogo.setXY(3, 4, true);
		assertEquals(jogo.numVizinhosVivos(4,4),1);
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}

}
