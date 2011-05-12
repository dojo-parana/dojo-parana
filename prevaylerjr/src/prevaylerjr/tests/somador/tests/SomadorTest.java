package prevaylerjr.tests.somador.tests;

import org.junit.Assert;
import org.junit.Test;

import prevaylerjr.tests.somador.Somador;

public class SomadorTest extends Assert {

	@Test
	public void soma() {
		Somador somador = new Somador();
		assertEquals(0, somador.total());
		
		somador.soma(5);
		assertEquals(5, somador.total());

		somador.soma(2);
		assertEquals(7, somador.total());

		somador.soma(-4);
		assertEquals(3, somador.total());
	}
	
}
