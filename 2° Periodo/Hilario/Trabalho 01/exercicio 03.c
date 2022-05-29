#include <stdio.h>

int main(){
    printf("Escreva um programa para ler um uma  temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius | C = ((F – 32)/9)*5 Salve com o seguinte formato:\n");
    
    float metros,mili;

    printf("Digite o valor em metros >> ");
    scanf("%f",&metros);

    mili = metros * 1000;

    printf("O valor %2.f transformado em militros = %2.f",metros,mili);
    
}