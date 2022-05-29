#Lucas Matheus de Souza Marques RA:  614491
#Andre genoti Dantas RA: 614084
#Luis Felipe Ribeiro Campos RA: 614432
print('Digite 2 numeros inteiros, depois some eles e descubra quandos "vai 1" a soma possue!!! ')
num = int(input('digite numeros inteiros de 3 digitos>>:'))
adicao= int(input('digite os numeros para somar unidades dezenas e centenas>>:'))
print(f'{num//100} ,{num%100//10} ,{num%10%100}')
print(f'{adicao // 100} ,{adicao % 100 // 10} ,{adicao % 10 % 100}')
centena = (num // 100) + (adicao // 100)
dezena = (num % 100 // 10) + (adicao % 100 // 10)
unidade = (num % 10 % 100) + (adicao % 10 % 100)
if centena >= 10 and dezena >= 10 and unidade >=10:
    print('3"vai 1"')
elif centena >= 10 and dezena >= 10 or dezena >= 10 and centena >= 10 or unidade >= 10 and dezena >= 10 or unidade >= 10 and centena >= 10 or centena >= 10 and unidade >= 10:
    print('2"vai 1')
elif centena >= 10 or dezena >= 10 or unidade >= 10:
    print('1 "vai 1"')
else:
    print('0"vai 1"')