package infra.testsupport.tests;

import infra.testsupport.CleanTestBase;

import java.io.File;

import org.junit.Test;


public class CleanTestBaseTest extends CleanTestBase {

	private static String _TMP_FOLDER_NAME;

	@Test
	public void consistentTmpFolderName() {
		assertEquals(tmpFolderName(), tmpFolder().getAbsolutePath());
	}

	
	@Test
	public void tmpFolderIsDeleted1() {
		_TMP_FOLDER_NAME = tmpFolderName();
		assertTrue(new File(_TMP_FOLDER_NAME).mkdirs());
	}

	
	@Test
	public void tmpFolderIsDeleted2() {
		if (wasRunInSeparateVM()) return;
		assertFalse(new File(_TMP_FOLDER_NAME).exists());
	}


	private boolean wasRunInSeparateVM() {
		return _TMP_FOLDER_NAME == null;
	}
	
}
