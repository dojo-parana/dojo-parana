package infra.testsupport;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

import org.junit.Assert;


public abstract class AssertUtils extends Assert {

	public static void assertFloat(float expected, float actual) {
		Assert.assertEquals(expected, actual, 0.001f);
	}

	
	public static <T> void assertContents(Iterable<T> actual, T... expected) {
		int i = 0;
		for (T actualItem : actual) {
			if (i == expected.length) {
				fail("Unexpected extra element '" + actualItem + "' at index " + i);
			}
			assertEquals("Different values at index " + i, expected[i], actualItem);
			i++;
		}
		assertEquals("Collections not same size", expected.length, i);
	}

	
	public static <T> void assertContentsInAnyOrder(Iterable<T> actual, T... expectedInAnyOrder) {
		Collection<T> collection = new ArrayList<T>();
		for (T element : actual) collection.add(element);
		
		for (T expected : expectedInAnyOrder)
			assertTrue("Expected element not found: " + expected, collection.contains(expected));
		
		assertEquals("Collections not same size", expectedInAnyOrder.length, collection.size());
	}


	public static void assertExists(File... files) {
		for (File file : files)
			assertTrue("File does not exist: " + file, file.exists());
	}

	
	public static void assertDoesNotExist(File... files) {
		for (File file : files)
			assertFalse("File should not exist: " + file, file.exists());
	}
	
	
	public static void assertStartsWith(byte[] expectedStart, byte[] actual) {
		byte[] actualStart = Arrays.copyOfRange(actual, 0, expectedStart.length);
		assertEquals(Arrays.toString(expectedStart), Arrays.toString(actualStart));
	}

}
