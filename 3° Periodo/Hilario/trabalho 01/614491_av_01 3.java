package testes;

import java.util.Scanner;

public class trabalho {
	public static void main(String[] args) {
		Scanner imput = new Scanner(System.in);
		
		int A[][] = new int[3][5];
				
		for(int i=0;i < 3;i++) {
			for(int j =0; j < 5; j++ ) {
				
				System.out.print("VALOR > ");
				int x = imput.nextInt();
				
				A[i][j] = x;
				
				}				
			}
		System.out.println("-----Matriz[3][5]-----");
		for(int l=0;l<3;l++) {
			for(int k=0;k<5;k++) {
				System.out.print(" "+ A[l][k]);
			}
			System.out.println("");
		}
		System.out.println("-----Matriz[3][5]-----");
		
		System.out.print("Digite um numero >");
		int valor = imput.nextInt();
		boolean Par_Impar = false;
		if (valor %2 == 0) {
			 Par_Impar = true;
		}		

		if (Par_Impar) {
			System.out.println("-*-*-*-*PARES-*-*-*-*");
			for(int l=0;l<3;l++) {
				for(int k=0;k<5;k++) {
					if(A[l][k] % 2 == 0) {
						System.out.print(" "+ A[l][k]);
					}
				}
				System.out.println("");
			}
			System.out.println("-*-*-*-*PARES-*-*-*-*");
		}else {
			System.out.println("-*-*-*-*IMPARES-*-*-*-*");
			for(int l=0;l<3;l++) {
				for(int k=0;k<5;k++) {
					if(A[l][k] % 2 != 0) {
						System.out.print(" "+ A[l][k]);
					}
				}
				System.out.println("");
			}
			System.out.println("-*-*-*-*IMPARES-*-*-*-*");	
		}

	}
}