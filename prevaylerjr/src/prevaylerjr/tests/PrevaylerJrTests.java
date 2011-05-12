package prevaylerjr.tests;


import infra.testsupport.CleanTestBase;

import java.io.IOException;

import org.junit.Test;

import prevaylerjr.PrevaylerJr;
import prevaylerjr.PrevaylerJr.Transacao;
import prevaylerjr.tests.somador.Somador;

public class PrevaylerJrTests extends CleanTestBase {

	private static final class Soma implements Transacao {
		@Override
			public void executa(Object sistema) {
				((Somador)sistema).soma(5);
			}
	}


	PrevaylerJr prevayler = createPrevayler();


	private PrevaylerJr createPrevayler()  {
		try {
			return new PrevaylerJr(new Somador(), tmpFolder());
		} catch (Exception e) {
			throw new IllegalStateException(e);
		}
	}
	
	/*public void criarSomador(int num, PrevaylerJr prev){
		Somador s = (Somador)prev.sistema();
		assertEquals(num, s.total());
	}
	
	@Test
	public void execucao() throws IOException {
		prevayler.execute(new Soma());
		criarSomador(5, createPrevayler());
		//PrevaylerJr prevayler2 = createPrevayler();
		criarSomador(5, createPrevayler());
	}*/
	
	
	@Test
	public void execucao() throws IOException {
		prevayler.execute(new Soma());
		
		Somador s = (Somador)prevayler.sistema();
		assertEquals(5, s.total());
		
		PrevaylerJr prevayler2 = createPrevayler();
		
		Somador s2 = (Somador)prevayler2.sistema();
		assertEquals(5, s2.total());
		
		prevayler2.execute(new Soma());
		assertEquals(10, s2.total());
		
		prevayler2.execute(new Soma());
		assertEquals(15, s2.total());
	}

}
