package trabalho;

import java.util.Random;
import java.util.ArrayList;
import java.util.Scanner;


public class funcao {
	
	ArrayList<Agenda>vetor = new ArrayList<Agenda>(); //Array para armazenas os 10 objetos
	Scanner input = new Scanner(System.in); // Scanner
	
	public void armazenaPessoa() {
			
		Random random = new Random();
		
		int controle = 0;
		do {
			
			System.out.println("Digite do objeto  "+ controle + 1);
			String nome1 = input.next();
			input.nextLine();
			
			Agenda p = new Agenda(); // Armazenar o objeta na agenda com os atributos
			p.setPosicao(controle);
			p.setNome(nome1);
			p.setIdade(random.nextInt(0,90));
			p.setAltura(random.nextFloat(1,2));
			vetor.add(p); // Armazena pessoa no array
						
			controle ++; 	
		}while(controle != 10 );

	}
		
	void removePessoa(){
		System.out.println("Digite o nome que deseja retirar da Agenda: ");
		String remover = input.next();
		
		for(Agenda i: vetor) {
			if(remover.equals(i.getNome())) {
				vetor.remove(i);
				break;
			}
		}
	}
	
	void BuscarPessoa() {
		System.out.println("Digite a nome: ");
		String letra = input.next();
		
		for(Agenda i: vetor) {
			if(letra.equals(i.getNome())) {
				System.out.println("Posiçao : "+i.getPosicao());
				break;
			}
		}
	}
	
	void imprimeAgenda() {
		for(Agenda i: vetor) {
			System.out.println("Posiçao : "+i.getPosicao()+"  Nome : "+i.getNome()+"  Idade : "+i.getIdade()+"  Altura : "+i.getAlura());
		}
	}
	
	void ImprimirPessoa(){
		System.out.println("Digite a posiçao que deseja ver : ");
		int op = input.nextInt();
		
		for(Agenda i: vetor) {
			if(op == i.getPosicao()) {
				System.out.println("Posiçao : "+i.getPosicao()+"  Nome : "+i.getNome()+"  Idade : "+i.getIdade()+"  Altura : "+i.getAlura());
				break;
			}
		}
	}
	
}