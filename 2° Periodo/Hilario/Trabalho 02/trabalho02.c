# include <stdio.h>

int main(){
    int cachorro_quente,bauru_simples,bauru_com_ovo,hamburguer,cheeseburguer,suco,refrigerante,codigo_de_barra;
    
    cachorro_quente =  100;
    bauru_simples = 101;
    bauru_com_ovo = 102;
    hamburguer = 103;
    cheeseburguer = 104;
    suco = 105;
    refrigerante = 106;

    printf("cachorro_quente =  100\nbauru_simples = 101\nbauru_com_ovo = 102\nhamburguer = 103\ncheeseburguer = 104\nsuco = 105\nrefrigerante = 106\n");

    float cont;

    do{
        printf("Digite o codigo do produto desejado >> ");
        scanf("%d",&codigo_de_barra);

        if (codigo_de_barra < 100 && codigo_de_barra > 106){
            printf("Voce Digitou um numero fora do limite!!");
        } else if (codigo_de_barra == 100){
            cont += 1.20;
        } else if (codigo_de_barra == 101){
            cont += 1.30;
        } else if (codigo_de_barra == 102){
            cont += 1.50;
        } else if (codigo_de_barra == 103){
            cont += 1.20;
        } else if (codigo_de_barra == 104){
            cont += 1.70;
        } else if (codigo_de_barra == 105){
            cont += 2.20;
        } else if (codigo_de_barra == 106){
            cont += 1.00;
        }

    } while (codigo_de_barra != 0);
    printf("O valor total a ser pago será de %0.2f",cont);
}