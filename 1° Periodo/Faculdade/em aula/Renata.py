print('digite um numero com 3 digitos!!!')
var1 = int(input('digite o valor'))
eq1 = var1 // 100
eq2 = (var1%100) //10
eq3 = var1%10
if var1 < 10 or var1 >= 1000 :
    print('O numero é Invalido')

elif var1%2==0 :
    soma = eq1 + eq2 + eq3
    print(f'a soma das centenas dezenas e unidade = {soma}')

else:
    sub = eq1 * eq2 * eq3
    print(f'a multiplicaçao das centenas dezenas e unidades = {sub}')

print('voce finalizou o exercicio!!')
print('os numeros tem que ter mais de 2 digitos e menos de 4 digitos!!')
print(f'{eq1} {eq2} {eq3}')