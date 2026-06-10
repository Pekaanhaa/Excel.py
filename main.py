print("lista de alunos aprovados/reprovados\n")


def se (condicao, valor_se_falso, valor_se_verdadeiro):
    return(valor_se_verdadeiro if condicao else valor_se_falso)
alunos = [
    ("Adriano", 40),
    ("Adriana", 60),
    ("Marcos", 94),
    ("Carlos", 70),
    ("Rebeca", 91),
    ("Roseane", 56),
    ("Tatiana", 54),
    ("Patrick", 51),
    ("Silas", 36),
    ("Bruna", 82),
    ("Bruno", 36),
    ("Ricardo", 62),
    ("Pedro", 65),
    ("José",  73),
    ("Maria", 91),
    ("João", 32)

]

print("Aluno\t\tNota\tSituação")
for aluno in alunos:
    nome, nota = aluno
    situacao = se(nota >= 70, "Reprovado 🔴", "Aprovado 🟢")
    print(f"{nome}\t\t{nota}\t{situacao}")

print("\n ------------------------------------")
reprovados = [aluno for aluno in alunos if aluno[1] < 70]
aprovados = [aluno for aluno in alunos if aluno[1] >= 70]



print(" total de alunos reprovados:", len(reprovados))
print(" total de alunos aprovados:", len(aprovados))

     
print("\n ----------Boletim Escolar-----------")

#   Não copiei do joãoooo teacher