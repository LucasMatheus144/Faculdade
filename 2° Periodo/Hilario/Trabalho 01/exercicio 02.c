#include <stdio.h>

int main(){
    printf("Escreva um programa que leia um valor em metros e o exiba convertido em  milímetros. Salve com o seguinte formato:\n");
 
    float metros,mili;

    printf("Digite o valor em metros >> ");
    scanf("%f",&metros);

    mili = metros * 1000;

    printf("O valor %f transformado em militros = %f",metros,mili);
    
}
