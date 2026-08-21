notas = [7.5, 8.0, 6.5, 9.0, 7.0]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
maior = max(notas)
menor = min(notas)

print("Média da turma:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)