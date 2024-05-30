
aluno = input("diga o nome do aluno: ")
disciplina = input("diga o nome da disciplina: ")
nota1 = int(input("qual foi a nota parcial: "))
nota2 = int(input("qual foi a nota bimestral: "))

media = (nota1 + nota2)/2

if media >= 6:
    situacao = "aprovado"
else:
    situacao = "reprovado"

print(aluno,"está",situacao,"na disciplina",disciplina)
