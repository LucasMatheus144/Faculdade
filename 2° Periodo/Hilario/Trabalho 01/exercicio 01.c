#include <stdio.h>

int main(){
    printf("Escreva um programa para receber 3  valores inteiros do usuário e mostrar a  sua média. Salve com o seguinte formato:\n");
    float a,b,c,media;
    printf("Digite o valor de A>");
    scanf("%f",&a);
    printf("Digite o valor de B>");
    scanf("%f",&b);
    printf("Digite o valor de C>");
    scanf("%f",&c);

    media = (a + b + c)/ 3;

    printf("A Media dos valores %2.f + %1.f + %1.f resulta em %f",a,b,c,media);
}
