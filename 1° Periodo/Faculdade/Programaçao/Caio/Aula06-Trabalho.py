# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
print('=-='*60)
#Exercicio 01
print('Faça  um  Programa  que  peça  a  temperatura  em  graus  Fahrenheit, transforme e mostre a temperatura em graus Celsius.')
f = int(input('Fahrenheit: '))
eq = (f-32) / 1.8
print(f'De {f}ºFahrenheit para Celsus resulta em {eq:.2f}º')
print('=-='*60)
#Exercicio 02
print('Faça  um  Programa  que  peça  a  temperatura  em  graus  Celsius, transforme e mostre em graus Fahrenheit.')
c = int(input('Celsus: '))
eq1 = (c *1.8) + 32
print(f'De {c}ºCelsus para Fahrenheit resulta em {eq1}')
print('=-='*60)
#Exercicio 03
print('Faça  um  programa  que  peça  o  tamanho  de  um  arquivo  para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule  e  informe  o  tempo  aproximado  de  download  do  arquivo usando este link (em minutos).')
a = float(input('Informe o tamanho do arquivo (em MB)>> '))
b = float(input('Informe a velocidade da internet(em MBPS) >> '))
c = a * 8
d = (c//b) / 60
print(f'O tempo aproximado de download do arquivo é de {d:.2f} minutos')
print('=-='*60)
#Exercicio 04
print('Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:●A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;●A mensagem "Reprovado", se a média for menor do que sete;●A mensagem "Aprovado com Distinção", se a média for igual a dez.')
nota,nota1 = float(input('Nota1: ')),float(input('Nota2: '))
media = (nota + nota1) / 2
if media == 10:
    print('O aluno foi APROVADO COM DISTINÇAO')
elif media >= 7:
    print('O aluno foi APROVADO')
else:
    print('Reprovado')