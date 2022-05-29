X = []
while True:
    num = int(input(f'Numero ---->> '))
    if len(X) == 5:
        break
    if num not in X:
        X.append(num)
    else:
        print('O numero ja esta na lista, digite novamente')
Y = []
while True:
    num = int(input(f'Numero ---->> '))
    if len(Y) == 5:
        break
    if num not in Y:
        Y.append(num)
    else:
        print('O numero ja esta na lista, digite novamente')
print(X)
print(Y)
soma = []
for c in range(5):
    soma.append(X[c] + Y[c])
prod = []
for k in range(5):
    prod.append(X[k] * Y[k])
dif = []
inter = []
for l in range(5):
        if X[l] not in Y[l]
            dif.append(X[l])
        else:
            inter.append(X[l])
uniao = []
for d in range(5):
    d.append(X[d])
    d.append(Y[d])