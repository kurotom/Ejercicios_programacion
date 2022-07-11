"""
Imprimir un banner usando -, ., | y WELCOME al centro.
N = numero natural impar
M = 3 * N
"""




print(len('---------.|.---------'))
print(len('------.|..|..|.------'))
print(len('---.|..|..|..|..|.---'))
print(len('-------WELCOME-------'))
print(len('---.|..|..|..|..|.---'))
print(len('------.|..|..|.------'))
print(len('---------.|.---------'))


# N, M = [7, 21]
N, M = [10, 30]
nMedium = 0
mMedium = 0
if type(N / 2) == float:
    nMedium = int(N / 2) + 1
else:
    nMedium = int(N / 2)

if type(M / 2) == float:
    mMedium = int(M / 2) + 1
else:
    mMedium = int(M / 2)

string = ''
a = 1
p = [i for i in range(N) if i % 2 != 0]
while a < nMedium:
    p1 = '.|.' * p[a -1]
    p2 = (M - len(p1)) // 2
    string += '-' * p2 + p1 + '-' * p2 + '\n'
    a += 1
string += '-' * ((M - 7) // 2) + 'WELCOME' + '-' * ((M - 7) // 2) + '\n'
while a > 1:
    p1 = '.|.' * p[a - 2]
    p2 = (M - len(p1)) // 2
    string += '-' * p2 + p1 + '-' * p2 + '\n'
    a -= 1

print(string)

