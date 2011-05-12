package infra.testsupport;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Method;
import java.util.Set;

import org.junit.After;
import org.junit.Before;
import org.junit.runner.RunWith;


/** A test that does not pollute the environment: it closes all files handles it opens, it does not leak threads, it does not write to the console (out and err). */
@RunWith(CleanTestRunner.class)
public abstract class CleanTestBase extends AssertUtils {

	static {
		System.setProperty("sneer.testmode", "true"); //USE ONLY FOR DEBUGGING. It is bad practice to use this otherwise.
	}
	
	private File _tmpFolder;
	private String _tmpFolderName;
	
	private Set<Thread> _activeThreadsBeforeTest;

	private final PrintStreamSentinel _outSentinel = new PrintStreamSentinel(System.out);
	private final PrintStreamSentinel _errSentinel = new PrintStreamSentinel(System.err);

	private final Object _failureMonitor = new Object();
	private Throwable _failure = null;
	private Method _failedMethod;

	
	protected File tmpFolder() {
		if (_tmpFolder == null)
			_tmpFolder = createFolder(tmpFolderName());

		return _tmpFolder;
	}

	
	private File createFolder(String folderName) {
		File result = new File(folderName);
		if (!result.exists())
			assertTrue("Unable to create tmp folder: " + result, result.mkdirs());
		return result;
	}

	
	protected String tmpFolderName() {
		if (_tmpFolderName == null) {
			String tmp = System.getProperty("java.io.tmpdir");
			_tmpFolderName = appendSeparator(tmp) + appendSeparator("cleantest") + this.getClass().getSimpleName() + System.nanoTime();
		}

		return _tmpFolderName;
	}

	
	private String appendSeparator(String path) {
		return path.endsWith(File.separator)
			? path
			: path + File.separator;
	}

	
	protected void assertTmpFilesExist(String... fileNames) {
		for (String fileName : fileNames)
			assertTmpFileExists(fileName);
	}

	
	protected void assertTmpFilesDontExist(String... fileNames) {
		for (String fileName : fileNames)
			assertTmpFileDoesntExist(fileName);
	}


	private void assertTmpFileExists(String fileName) {
		File file = new File(tmpFolder(), fileName);
		assertExists(file);
	}

	
	private void assertTmpFileDoesntExist(String fileName) {
		File file = new File(tmpFolder(), fileName);
		assertDoesNotExist(file);
	}

	
	@Before
	public void beforeCleanTest() {
		_activeThreadsBeforeTest = Thread.getAllStackTraces().keySet();
		
		System.setOut(_outSentinel);
		System.setErr(_errSentinel);
	}

	
	@After
	public void afterCleanTest() {
		recoverConsole();

		if (_failure != null) {
			afterFailedtest(_failedMethod, _failure);
			return;
		}
		
		checkThreadLeak();
		deleteTmpFolder();
		checkConsolePollution();
	}
	
	
	/** To be subclassed optionally. */
	protected void afterFailedtest(Method method, Throwable thrown) {}

	private void recoverConsole() {
		System.setOut(_outSentinel._delegate);
		System.setErr(_errSentinel._delegate);
	}
	
	private void checkThreadLeak() {
		Set<Thread> activeThreadsAfterTest = Thread.getAllStackTraces().keySet();

		for (Thread thread : activeThreadsAfterTest)
			stopIfNecessary(thread);
	}

	
	@SuppressWarnings("deprecation")
	private void stopIfNecessary(Thread thread) {
		if(_activeThreadsBeforeTest.contains(thread)) return;
		if (waitForTermination(thread)) return;
		if (thread.getName().indexOf("AWT") != -1) return; //Fix: Check for leaking Gui resources too.
		if (thread.getName().indexOf("Java2D") != -1) return; //Fix: Check for leaking Gui resources too.

		final LeakingThreadStopped plug = new LeakingThreadStopped(thread, "" + thread + " was leaked by test: " + this.getClass() + " and is now being stopped!");
		thread.stop(plug);
		
		throw new IllegalStateException(plug);
	}

	
	private boolean waitForTermination(Thread thread) {
		long t0 = System.currentTimeMillis();
		while (true) {
			if (thread.getState() == Thread.State.TERMINATED) return true;
			if (System.currentTimeMillis() - t0 > 2000) return false;
			System.gc();
			sleep(10);
		}
	}

	
	private void sleep(long millis) {
		try {
			Thread.sleep(millis);
		} catch (InterruptedException e) {
			throw new IllegalStateException(e);
		}
	}

	
	private void checkConsolePollution() {
		_outSentinel.complainIfUsed();
		_errSentinel.complainIfUsed();
	}

	
	private void deleteTmpFolder() {
		if (_tmpFolderName == null) return;

		tryToClean(new File(_tmpFolderName));
		_tmpFolderName = null;
		_tmpFolder = null;
	}

	
	private void tryToClean(File tmp) {
		long t0 = System.currentTimeMillis();
		while (true) {
			try {
				deleteFolder(tmp);
				return;
			} catch (IOException e) {
				if (System.currentTimeMillis() - t0 > 1000) {
					throw new IllegalStateException(e);
				}
				System.gc();
			}
		}
	}
	
	
	class LeakingThreadStopped extends Throwable {
		public LeakingThreadStopped(Thread leakingThread, String message) {
			super(message);
			setStackTrace(leakingThread.getStackTrace());
		}

		@Override
		public synchronized Throwable fillInStackTrace() {
			return this;
		}
		
		private static final long serialVersionUID = 1L;
	}

	
	void deleteFolder(File folder) throws IOException {
		if (!folder.exists()) return;
		if (!folder.isDirectory()) 
			throw new IllegalArgumentException(folder.getAbsolutePath() + " is not a folder");

		recursiveDelete(folder);

		if (!folder.delete()) 
			throw new IOException("Unable to delete folder: " + folder.getAbsolutePath());
	}

	
	private void recursiveDelete(File folder) throws IOException, FileNotFoundException {
		for (File file : folder.listFiles()) {
			if (!file.exists()) 
				throw new FileNotFoundException("File does not exist: " + file.getAbsolutePath());
			
			if (file.isFile() && !file.delete()) 
				throw new IOException(("Unable to delete file: " + file.getAbsolutePath()));
			
			deleteFolder(file);
		}
	}


	void failedWith(Method method, Throwable thrown) {
		if (_failure != null) return;
		
		String message = thrown.getMessage();
		if (message != null && message.startsWith("test timed out")) //Kent, Erich, please improve the JUnit API for tests with timeouts. JUnit4ClassRunner.invokeTestMethod hides the test instance and the roadie. TestRunner and TestMethod parallel hierarchies is the only (clumsy) way to get close to what one needs. Klaus.
			tryToWaitForTheFailureFromTheActualTestThread(method, thrown);
		else
			keepFailure(method, thrown);
	}

	
	private void keepFailure(Method method, Throwable thrown) {
		synchronized (_failureMonitor) {
			_failure = thrown;
			_failedMethod = method;
			_failureMonitor.notifyAll();
		}
	}

	
	private void tryToWaitForTheFailureFromTheActualTestThread(Method method, Throwable thrown) {
		synchronized (_failureMonitor) {
			try {
				_failureMonitor.wait(5000);
			} catch (InterruptedException e) {
				throw new IllegalStateException(e);
			}
			if (_failure == null) keepFailure(method, thrown);
		}
	}

	
	protected void createTmpFiles(String... fileNames) throws IOException {
		for (String fileName : fileNames)
			createTmpFile(fileName);
	}

	protected File createTmpFile(String fileName, String contents) throws IOException {
		File file = createTmpFile(fileName);
		write(file, contents);
		return file;
	}
	
	protected File createTmpFile(String fileName) throws IOException {
		File file = newTmpFile(fileName);
		if (!file.getParentFile().exists())
			assertTrue("Unable to mkdirs: " + file.getParentFile(), file.getParentFile().mkdirs());
		assertTrue(file.createNewFile());
		return file;
	}

	
	protected File newTmpFile() {
		return newTmpFile("tmp" + System.nanoTime());
	}

	
	protected File newTmpFile(String fileName) {
		return new File(tmpFolder(), fileName);
	}

	
	protected void createTmpFilesWithFileNameAsContent(String... fileNames) throws IOException {
		for (String fileName : fileNames)
			createTmpFileWithFileNameAsContent(fileName);
	}

	
	protected File createTmpFileWithFileNameAsContent(String fileName) throws IOException {
		return createTmpFile(fileName, fileName);
	}


	private void write(File file, String contents)
			throws FileNotFoundException, IOException,
			UnsupportedEncodingException {
		FileOutputStream fileOutputStream = new FileOutputStream(file);
		try {
			fileOutputStream.write(contents.getBytes("UTF-8"));
		} finally {
			fileOutputStream.close();
		}
	}

}


class PrintStreamSentinel extends PrintStream {
	
	IllegalStateException _exception;
	final PrintStream _delegate;
	
	
	PrintStreamSentinel(PrintStream delegate) {
		super(delegate);
		_delegate = delegate;
	}
	
	
	@Override public void write(byte[] buf, int off, int len) {
		try {
			throw new IllegalStateException("Test would have passed if it were not polluting the console.");
		} catch (IllegalStateException e) {
			_exception = e;
		}
		super.write(buf, off, len);
	}
	
	
	void complainIfUsed() {
		if (_exception != null)	throw _exception;
	}
	
}
