a = [1,2,3]
# 2
a = [80,30,30]

# Sumar los indices pares y restar los indices impares
par = []
impar = []
for i in range(len(a)):
    if i % 2 == 0:
        par.append(a[i])
    else:
        impar.append(a[i])
print(sum(par) - sum(impar))
