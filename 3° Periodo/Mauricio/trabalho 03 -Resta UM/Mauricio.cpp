#include <stdio.h>
#include <stdlib.h>
#include <conio.h>



struct dados{
	int info;
	struct dados *prox;
};

typedef struct dados SI;




void criar_lista(SI **Inicio, SI **Fim){
	*Inicio = NULL;
	*Fim = NULL;
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



void Inserir_Inicio(SI **Inicio,int valor,SI **Fim){
	SI *p;

	p = (SI *)calloc(1,sizeof(SI));
	p->info = valor;
	p->prox = *Inicio;



	if( *Inicio == NULL){
		*Fim = p;
		}
	*Inicio = p;
}



void Rem_Inicio(SI **Inicio, SI **Fim)
{
	SI *p;

	p = *Inicio;
	if ( p->prox==NULL)
	{
		*Inicio = NULL;
		*Fim = NULL;
	}
	else
		*Inicio = p->prox;

	free(p);
}
void Rem_Fim(SI **Inicio, SI **Fim)
{
	SI *p, *q;

	p = *Fim;
	if (p==*Inicio){
		*Inicio = NULL;
		*Fim = NULL;
	}else{
		q =*Inicio;
		while (q->prox != *Fim)
			q = q->prox;

			q->prox = NULL;
			*Fim = q;
	}
	free(p);
}




SI * Consulta(SI *Inicio, int val)
{
	SI *p;

	p = Inicio;

	while (p!=NULL && p->info!= val)
		p = p->prox;


	return p;
}



void Rem_Meio(SI *Inicio, SI *r)
{
	SI *q;

	q = Inicio;
	while (q->prox!= r)
		q = q->prox;

		q->prox = r->prox;

	free(r);

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



void remover(SI **Inicio, int val){
	SI *Aux,*remove = NULL;



	if(*Inicio){
		if((*Inicio)->info == val){
		remove = *Inicio;
		}
	}else{
		Aux = *Inicio;
	while(Aux->prox && Aux->prox->info != val){
		Aux = Aux->prox;
	}
	if(Aux->prox){
		remove = Aux->prox;
		Aux->prox = remove->prox;
		}
	}
	free(remove);
}



void Remover_Repetido(SI **Inicio, SI **Fim){
	SI *auxiliar, *p, *teste;

	auxiliar = *Inicio; //auxiliar

	p = *Inicio; //Inicio

	while(p != NULL){ 
	auxiliar = p->prox; 
		while(auxiliar != NULL){ 
			if(p->info == auxiliar->info){
				if (auxiliar != *Fim){
					teste = auxiliar->prox;
					Rem_Meio(*Inicio, auxiliar);
					auxiliar = teste;
				}else{
					Rem_Fim(Inicio, Fim);
					auxiliar = NULL;
					}
		}else
		auxiliar = auxiliar->prox;
		}
	p = p->prox;//proximo p
	}

}


SI * Resta_Um (SI ** Inicio, SI ** Fim, int val){
	SI *p, *q;
	int cont = 1;
	
	p = *Inicio;
	
	while (*Inicio != *Fim){
		while (p != NULL){
			if (cont != val){
				q = p;
				p = p->prox;
				cont ++;
			}else{
				if (p == *Inicio){
				*Inicio = p->prox;
				
				free(p);
				
				p = *Inicio;
			}else if (p == *Fim){
				q->prox = NULL;
				*Fim = q;
				
				free(p);
				
				p = *Inicio;
			}else{
				q->prox = p->prox;
				
				free(p);
				
				p = q->prox;
			}
		cont = 1;
		}
	}
	p = *Inicio;
	}
	return *Inicio;
}



main(){
	SI *Inicio, *Fim, *r;
	int op,val;

	criar_lista(&Inicio,&Fim);

	do{
	system("cls");
	puts("0 - Encerrar o Programa!");
	puts("1 - Imprimir Lista");
	puts("2 - Consultar valor");
	puts("3 - Inserir valor");
	puts("4 - Remover Inicio");
	puts("5 - Remover meio");
	puts("6 - Inserir Ordenado");
	puts("7 - Remover valores repetidas");
	puts("8 - Resta um!");

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

	case 2: printf("\nDigite o valor a procurar:");
		scanf("%d", &val);

		r = Consulta(Inicio, val);

		if (r==NULL)
			printf("\nValor nao existe na lista!");
		else
			printf("\nValor encontrado: %d", r->info);

		getch();
		break;

	case 3:printf("\nDigite o valor a inserir:");
		scanf("%d", &val);
		Inserir_Inicio(&Inicio, val,&Fim);
		getch();
		break;

	case 4:if (Inicio == NULL)
			printf("\nLista Vazia!");
		else
		{
			printf("\nRemovendo o valor %d", Inicio->info);
			Rem_Inicio(&Inicio, &Fim);
		}
		getch();
		break;



	case 5: printf("\nDigite o valor a procurar:");
		scanf("%d", &val);

		r = Consulta(Inicio, val);

		if (r==NULL)
			printf("\nValor nao existe na lista!");
		else
			Rem_Meio(Inicio,r);

			getch();
			break;

	case 6:printf("\nDigite o valor a inserir:");
		scanf("%d", &val);
		Inserir_Ordenado(&Inicio, val);
		getch();
		break;



	case 7:printf("Removendo valor repetido");
		Remover_Repetido(&Inicio, &Fim);
		
		getch();
		break;

	case 8:printf("\nDigite um valor");
		   scanf("%d",&val);
		   r = Consulta(Inicio,val);
		   if(r == NULL){
		   		printf("\nValor nao existe na lista!");
		   }else{
		   		Resta_Um(&Inicio,&Fim,val);
		   }
		   
		}
	}while(op != 0);
}
