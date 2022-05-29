package trabalho;

import java.util.Scanner;

public class Principal {
	
	public static void main(String[] args) {
		
		funcao funcao = new funcao();
		Scanner input = new Scanner(System.in); // Scanner

		int op;
		
		do {
			System.out.println("");

			System.out.println(" 0- Encerrar o programa");
			System.out.println(" 1- Adicionar 10 pessoas na Agenda");
			System.out.println(" 2- Imprimir Agenda");
			System.out.println(" 3- Imprimir Pessoa");
			System.out.println(" 4- Imprimir posiçao da pessoa");
			System.out.println(" 5- Remover Pessoa da Agenda");
			
			System.out.println("");

			
			System.out.println("Digite qual opição deseja realizar : ");
			op = input.nextInt();
			
			System.out.println("");

			switch(op) {
			case 1: System.out.println("Digite os nomes para adicionar na Agenda com suas respectivas informaçõs");
				funcao.armazenaPessoa();
				break;
				
			case 2:System.out.println("Imprimindo Agenda");
				funcao.imprimeAgenda();
				break;
				
			case 3:System.out.println("Imprimir Pessoa especifica da agenda");
				funcao.ImprimirPessoa();
				break;
				
			case 4:System.out.println("Imprimi posiçao da Pessoa na Agenda");
				funcao.BuscarPessoa();
				break;

			case 5: System.out.println("Removendo Pessoa da Agenda");
				funcao.removePessoa();
				break;
			}
		
		}while(op != 0);
	}

}
