import math

#nome::::Lucas Matheus de Souza Marques
# RA:::::614491
            #exercicio 01
#'A rua Tenório Quadros e a avenida Teófilo Silva, ambas retilíneas,  cruzam-se conforme um ângulo de 30º. O posto de gasolina Estrela do Sul  encontra-se na avenida Teófilo Silva a 4 000 m do citado cruzamento. Sabendo que o percurso do posto Estrela do Sul até a rua tenório quadros forma um ângulo de 90° no ponto de encontro do posto com a rua Teófilo Silva, determine em quilômetros, a distância entre o posto de gasolina Estrela do Sul e a rua Tenório Quadros?
print('30°')
print('4000m')
print('90°')
eq = math.tan(math.radians(30))
co = 4000*eq
eq = co/1000
print(f'o resultando é {co:.1f}')
print('=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>')

#Um avião levanta voo sob um ângulo constante de 20º. Após percorrer 2 000 metros em linha reta, qual será a altura atingida pelo avião, aproximadamente?
print('20° costante')
print('apos percorrer 2000m')
form = math.sin(math.radians(20))
co = 2000 * eq
eq1 = co/1000
print(f'o resultando é {form :.1f} metros')
print('=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>')

              #exercicio 03
#Faça um programa que lê a distância de um aeroporto a um prédio (x metros), o tamanho do prédio (y metros), a altura de segurança (z metros) e o ângulo que o avião sobe (w graus). Ao final, diga se o avião pode decolar ou não.
a = float(input('digite x em metros '))
b = float(input('digite y em metros do predio'))
c = int(input('digite w graus'))
d = float(input('digite z metros minima da altura'))
if b<=a:
    print('Havera  atrito entre o aviao e o predio')
else:
    print('Nao havera atrito ')
print('=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>')

    #exercicio 04
#Um drone irá decolar na Rua João e deve pousar na Rua Mário fazendo um trajeto em linha reta, como ilustrado na figura. Sabe-se que o drone tem autonomia de m metros, que a distância do ponto que o drone decolou até a rua Mário é x metros e a distância da Rua João até o destino do drone na rua Mário é y metros. Faça um programa que lê os valores m, x e y e mostra se o drone conseguirá chegar ao destino.
x = float(input('digite a distancia ate o final da rua'))
y = float(input('digite a distancia da rua ate o drone'))
m = float(input('digite a autonomia do drone'))
hip = math.hypot(x,y)
if hip>=m:
    print('Nao via chegar ate o destino')
else:
    print('Ira chegar no destino ')
