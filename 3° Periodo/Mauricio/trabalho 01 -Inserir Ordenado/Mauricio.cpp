#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

struct dados{
	int info;
	struct dados *prox;
};

typedef struct dados SI;


void criar_lista(SI **Inicio){
	*Inicio = NULL;
}

void Imprime_Lista(SI *Inicio){
	SI *p;
	
	p = Inicio;
	printf("\nLista\n");
	while(p != NULL){
		printf("%d --> ",p->info);
		p = p->prox;
	}
	printf("NULL\n");
}

void Inserir_Inicio(SI **Inicio,int valor){
	SI *p;
	
	p = (SI *)calloc(1,sizeof(SI));
	p->info = valor;
	p->prox = *Inicio;
	*Inicio = p;	
}

void Inserir_Ordenado(SI **Inicio,int valor){
	SI *auxiliar,*p;
	
	p = (SI*)calloc(1,sizeof(SI));
	p->info = valor;
	
	if(*Inicio == NULL){
		p->prox = NULL;
		*Inicio = p;
	}else if(p->info < (*Inicio)->info){
		p->prox = *Inicio;
		*Inicio = p;		
	}else{
		auxiliar = *Inicio;
		while(auxiliar->prox && p->info > auxiliar->prox->info){
			auxiliar = auxiliar->prox;
		}
		p->prox = auxiliar->prox;
		auxiliar->prox = p;
	}
}

main(){
	SI *Inicio;
	int op,val;
	
	criar_lista(&Inicio);
	
	do{
		system("cls");
		puts("0 - Encerrar o Programa!");
		puts("1 - Imprimir Lista");
		puts("2 - Inserir valor");
		puts("3 - Inserir Ordenado");
		
		
		printf("\nDigite a sua opcao --> ");
		scanf("%d",&op);
		
		switch(op){
			
			case 1:if(Inicio == NULL){
				printf("\nLista Vazia!");	
			}else{
				Imprime_Lista(Inicio);
			}
				getch();
				break;
			
			case 2:printf("\nDigite o valor a inserir:");
			        scanf("%d", &val);
			        Inserir_Inicio(&Inicio, val);
			    getch();
			    break;
			
			case 3:printf("\nDigite o valor a inserir:");
			       scanf("%d", &val);
			       Inserir_Ordenado(&Inicio, val);
				getch();
				break;
		}
	}while(op != 0);
}
