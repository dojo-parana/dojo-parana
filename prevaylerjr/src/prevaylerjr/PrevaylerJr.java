package prevaylerjr;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class PrevaylerJr {

	private final Object _sistema;
	private ObjectOutputStream  _arquivo;

	public interface Transacao extends Serializable {
		void executa(Object sistema);
	}

	public PrevaylerJr(Object sistema, File folderDeDados) throws FileNotFoundException, IOException, Exception {
		_sistema = sistema;

		File arq = new File(folderDeDados, "transacoes.txt");
		restauraSistema(arq);
		
		_arquivo = new ObjectOutputStream(new FileOutputStream(arq));
	}

	private void restauraSistema(File arq) throws IOException, FileNotFoundException,
			ClassNotFoundException {
		if(!arq.exists())
			return;
		
		ObjectInputStream arquivoLeitura = new ObjectInputStream(new FileInputStream(arq));
		((Transacao)arquivoLeitura.readObject()).executa(_sistema);
		
	}

	public Object sistema() {
		return _sistema;
	}

	public void execute(Transacao transacao) throws IOException {
		_arquivo.writeObject(transacao);
		_arquivo.close();
		transacao.executa(_sistema);
		
	}

}
